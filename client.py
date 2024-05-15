import grpc
import recommendations_pb2
import recommendations_pb2_grpc

def run():
    # Conectar al servidor gRPC
    channel = grpc.insecure_channel('localhost:50052')
    stub = recommendations_pb2_grpc.RecommendationServiceStub(channel)

    # Crear un mensaje de solicitud
    response = stub.GetRecommendations(recommendations_pb2.AnalysisResult(tuit_id="12345", analysis="Sentimiento positivo"))

    # Imprimir la respuesta del servidor
    print("Recomendaciones recibidas: ", response.recommendations)
    print("tuit numero: ",response.tuit_id)

if __name__ == '__main__':
    run()
