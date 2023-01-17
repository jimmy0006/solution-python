from concurrent import futures
import logging

import grpc
import sound_pb2
import sound_pb2_grpc


class File(sound_pb2_grpc.FileServicer):
	
    def Define(self, request, context):
        print(request.country)
        return sound_pb2.SoundResponse(res='Hello, %s!' % request.country)

    def Connect(self, request, context):
        print(request.ping)
        return sound_pb2.Pong(pong='%s Pong!' % request.ping)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sound_pb2_grpc.add_FileServicer_to_server(File(), server)
    server.add_insecure_port('[::]:8080')
    print("server on port 8080")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()