from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.general import User
from diagrams.aws.integration import SNS, SQS
from diagrams.aws.mobile import APIGateway
from diagrams.k8s.compute import Pod
from diagrams.onprem.ci import Jenkins

graph_attr = {
    "fontsize": "28",
    "fontname": "Helvetica",
    "style": "rounded",
    "dpi": "150",
    "splines": "true"
}

edge_attr = {
    "minlen": "3"
}

with Diagram("Example diagram", outformat=["png", "pdf"], show=False, graph_attr=graph_attr, edge_attr=edge_attr):

    user = User("user")

    api_gateway = APIGateway("GTW")

    service_1 = Pod("service-1")
    service_2 = Pod("service-2")
    service_3 = Pod("service-3")

    sns_1 = SNS("sns-1")
    sns_2 = SNS("sns-2")

    sqs_3 = SQS("sqs-3")

    with Cluster("SNS1 - Destination"):

        sqs_1 = SQS("sqs-1")
        sqs_2 = SQS("sqs-2")

        cluster_1 = [sqs_1, sqs_2]

    # beginning of the diagram

    user >> api_gateway >> service_1

    service_1 >> sns_1

    sns_1 >> cluster_1

    sqs_1 >> service_2

    sqs_2 >> service_3

    service_2 >> sns_2 >> sqs_3
