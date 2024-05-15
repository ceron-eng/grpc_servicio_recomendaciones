from concurrent import futures
import grpc
import recommendations_pb2
import os
import recommendations_pb2_grpc
from builder import generate_recommendation  # Importa la función


port = os.getenv('PORT', '50052')

class RecommendationService(recommendations_pb2_grpc.RecommendationServiceServicer):
    def GetRecommendations(self, request, context):
        # Obtener recomendaciones usando la función importada
         # Aquí usamos la variable simulada
        #analysis_data = simulated_analysis["analysis"]
        # Convertir el diccionario a string para simular una transmisión real
        #analysis_str = f"Sentimiento: {analysis_data['sentiment']}"
        # Obtener recomendaciones usando la función importada
        #recommendations = generate_recommendation(analysis_str)
        recommendations = generate_recommendation(request.analysis)
        return recommendations_pb2.RecommendationResponse(tuit_id=request.tuit_id,recommendations=[recommendations])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationServiceServicer_to_server(RecommendationService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print("Server running on port 50052")  # Mensaje de confirmación
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
