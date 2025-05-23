"""
Module for interacting with the backend.
"""

from typing import Any, Dict

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


class Backend:
    def __init__(self, graphql_url: str):
        """
        Backend class for interacting with the backend.

        Args:
            graphql_url (str): URL of the GraphQL endpoint.
        """
        self._graphql_url: str = graphql_url

    @property
    def graphql_url(self) -> str:
        """
        GraphQL endpoint URL.
        """
        return self._graphql_url

    def _get_client(
        self,
        headers: Dict[str, str] = None,
        fetch_schema_from_transport: bool = False,
    ) -> Client:
        """
        Get a GraphQL client.

        Args:
            headers (Dict[str, str], optional): Headers to be passed to the client. Defaults to
                None.
            fetch_schema_from_transport (bool, optional): Whether to fetch the schema from the
                transport. Defaults to False.

        Returns:
            Client: GraphQL client.
        """
        transport = RequestsHTTPTransport(
            url=self.graphql_url, headers=headers, use_json=True
        )
        return Client(
            transport=transport,
            fetch_schema_from_transport=fetch_schema_from_transport,
        )

    def _execute_query(
        self,
        query: str,
        variables: Dict[str, str] = None,
        client: Client = None,
        headers: Dict[str, str] = None,
        fetch_schema_from_transport: bool = False,
    ) -> Dict[str, Any]:
        """
        Execute a GraphQL query.

        Args:
            query (str): GraphQL query.
            variables (Dict[str, str], optional): Variables to be passed to the query. Defaults
                to None.
            client (Client, optional): GraphQL client. Defaults to None.
            headers (Dict[str, str], optional): Headers to be passed to the client. Defaults to
                None.
            fetch_schema_from_transport (bool, optional): Whether to fetch the schema from the
                transport. Defaults to False.

        Returns:
            Dict: GraphQL response.
        """
        if not client:
            client = self._get_client(
                headers=headers,
                fetch_schema_from_transport=fetch_schema_from_transport,
            )
        return client.execute(gql(query), variable_values=variables)

    def _get_token(self, email: str, password: str) -> str:
        """
        Get JWT token for authentication.
        """
        mutation = """
            mutation ($email: String!, $password: String!) {
                tokenAuth(email: $email, password: $password) {
                    token
                }
            }
        """
        variables = {"email": email, "password": password}
        response = self._execute_query(mutation, variables)
        return response["tokenAuth"]["token"]

    def _get_dataset_id_from_name(self, gcp_dataset_id):
        query = """
            query ($gcp_dataset_id: String!){
                allCloudtable(gcpDatasetId: $gcp_dataset_id) {
                    edges {
                        node {
                                table {
                                    dataset {
                                        _id
                                    }
                            }
                        }
                    }
                }
            }
        """

        variables = {"gcp_dataset_id": gcp_dataset_id}
        response = self._execute_query(query=query, variables=variables)
        r = (
            {}
            if response is None
            else self._simplify_graphql_response(response)
        )
        if r.get("allCloudtable", []) != []:
            return (
                r.get("allCloudtable")[0]
                .get("table")
                .get("dataset")
                .get("_id")
            )
        msg = f"{gcp_dataset_id} not found. Please create the metadata first in {self.graphql_url}"
        raise Exception(msg)

    def _get_table_id_from_name(self, gcp_dataset_id, gcp_table_id):
        query = """
            query ($gcp_dataset_id: String!, $gcp_table_id: String!){
                allCloudtable(gcpDatasetId: $gcp_dataset_id, gcpTableId: $gcp_table_id) {
                    edges {
                        node {
                                table {
                                    _id
                            }
                        }
                    }
                }
            }
        """

        if gcp_dataset_id:
            variables = {
                "gcp_dataset_id": gcp_dataset_id,
                "gcp_table_id": gcp_table_id,
            }

            response = self._execute_query(query=query, variables=variables)
            r = (
                {}
                if response is None
                else self._simplify_graphql_response(response)
            )
            if r.get("allCloudtable", []) != []:
                return r.get("allCloudtable")[0].get("table").get("_id")
        msg = f"No table {gcp_table_id} found in {gcp_dataset_id}. Please create in {self.graphql_url}"
        raise Exception(msg)

    def get_dataset_config(self, gcp_dataset_id: str) -> Dict[str, Any]:
        """
        Get dataset configuration.

        Args:
            dataset_id (str): The ID for the dataset.

        Returns:
            Dict: Dataset configuration.
        """
        query = """
            query ($dataset_id: ID!){
                allDataset(id: $dataset_id) {
                    edges {
                        node {
                            slug
                            name
                            descriptionPt
                            createdAt
                            updatedAt
                            themes {
                                edges {
                                    node {
                                        namePt
                                    }
                                }
                            }
                            tags {
                                edges {
                                    node {
                                        namePt
                                    }
                                }
                            }
                            organization {
                                namePt
                            }
                        }
                    }
                }
            }

        """
        variables = {
            "dataset_id": self._get_dataset_id_from_name(
                gcp_dataset_id=gcp_dataset_id
            )
        }
        response = self._execute_query(query=query, variables=variables)
        return self._simplify_graphql_response(response).get("allDataset")[0]

    def get_table_config(
        self, gcp_dataset_id: str, gcp_table_id: str
    ) -> Dict[str, Any]:
        """
        Get table configuration.

        Args:
            dataset_id (str): The ID for the dataset.
            table_id (str): The ID for the table.

        Returns:
            Dict: Table configuration.
        """

        query = """
            query ($table_id: ID!) {
                allTable (id: $table_id) {
                    edges {
                        node {
                            slug,
                            name,
                            description,
                            cloudTables {
                                edges {
                                    node {
                                        gcpProjectId
                                        gcpDatasetId
                                        gcpTableId
                                    }
                                }
                            }
                            dataset {
                                slug,
                                name,
                                description,
                                themes {
                                    edges {
                                        node {
                                            slug,
                                            name,
                                        }
                                    }
                                },
                                tags {
                                    edges {
                                        node {
                                            slug
                                            name
                                        }
                                    }
                                }
                            },
                            status {
                                name,
                                slug
                            },
                            license {
                                name,
                                slug
                            },
                            pipeline {
                                githubUrl
                            },
                            publishedBy {
                                firstName,
                                lastName,
                                email
                            },
                            dataCleanedBy {
                                firstName,
                                lastName,
                                email
                            },
                            dataCleaningDescription,
                            dataCleaningCodeUrl,
                            rawDataUrl,
                            auxiliaryFilesUrl,
                            architectureUrl,
                            columns {
                                edges {
                                    node {
                                        name,
                                        description
                                    }
                                }
                            }
                        }
                    }
                }
            }
        """
        variables = {
            "table_id": self._get_table_id_from_name(
                gcp_dataset_id=gcp_dataset_id, gcp_table_id=gcp_table_id
            )
        }
        response = self._execute_query(query=query, variables=variables)
        return self._simplify_graphql_response(response).get("allTable")[0]

    def _get_tables_for_dataset(self, dataset_id: str) -> Dict[str, Any]:
        """
        Gets all table slugs for a dataset.
        """
        dataset_id = self._get_dataset_id_from_name(dataset_id)
        query = """
            query ($dataset_id: ID!) {
                allDataset (id: $dataset_id) {
                    edges {
                        node {
                            tables {
                                edges {
                                    node {
                                        _id,
                                        slug,
                                        cloudTables {
                                            edges {
                                                node {
                                                    gcpTableId
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        """
        variables = {"dataset_id": dataset_id}
        response = self._execute_query(query=query, variables=variables)
        return self._simplify_graphql_response(response).get("allDataset")[0]

    def _get_status_id(self, status_slug: str) -> str:
        query = """
            query ($status_slug: String!) {
                allStatus (slug: $status_slug) {
                    edges {
                        node {
                            _id
                        }
                    }
                }
            }
        """
        variables = {"status_slug": status_slug}
        response = self._execute_query(query=query, variables=variables)
        statuses = self._simplify_graphql_response(response).get("allStatus")
        if len(statuses) == 0:
            raise Exception(f"Status {status_slug} not found")
        return statuses[0].get("_id")

    def modify_status_for_table(
        self,
        gcp_dataset_id: str,
        gcp_table_id: str,
        status_slug: str,
        email: str = None,
        password: str = None,
        token: str = None,
    ):
        # Assert that either (email and password) or token is provided
        if (email is None or password is None) and token is None:
            raise Exception(
                "Either (email and password) or token must be provided to modify status"
            )
        # If token is not provided, get token from email and password
        if token is None:
            token = self._get_token(email, password)
        table_id = self._get_table_id_from_name(gcp_dataset_id, gcp_table_id)
        status_id = self._get_status_id(status_slug)
        mutation = """
            mutation ($table_id: ID!, $status_id: ID!) {
                CreateUpdateTable(input: {
                    id: $table_id,
                    status: $status_id
                }) {
                    errors {
                        field,
                        messages
                    }
                }
            }
        """
        variables = {"table_id": table_id, "status_id": status_id}
        headers = {
            "Authorization": f"Bearer {token}",
        }
        response = self._simplify_graphql_response(
            self._execute_query(
                query=mutation, variables=variables, headers=headers
            )
        )
        errors = response.get("CreateUpdateTable").get("errors")
        if errors:
            raise Exception(errors)

    def _simplify_graphql_response(self, response: dict) -> dict:
        """
        Simplify the graphql response
        Args:
            response: the graphql response
        Returns:
            dict: the simplified graphql response
        """
        if response == {}:  # pragma: no cover
            return {}

        output_ = {}

        for key in response:
            try:
                if (
                    isinstance(response[key], dict)
                    and response[key].get("edges") is not None
                ):
                    output_[key] = [
                        v.get("node")
                        for v in list(
                            map(
                                self._simplify_graphql_response,
                                response[key]["edges"],
                            )
                        )
                    ]
                elif isinstance(response[key], dict):
                    output_[key] = self._simplify_graphql_response(
                        response[key]
                    )
                else:
                    output_[key] = response[key]
            except TypeError as e:
                print(f"Erro({e}): {key} - {response[key]}")
        return output_
