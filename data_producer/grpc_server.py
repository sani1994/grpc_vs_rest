from concurrent import futures

import grpc

import data_stream_service_pb2_grpc
import data_stream_service_pb2
from db_utils.db_helper import UserDB


class UserDataServicer(data_stream_service_pb2_grpc.DataStreamServicer):
    def GetUserByID(self, request, context):
        _data = UserDB().get_user(id=request.id)[0]
        data = data_stream_service_pb2.UserData()
        data.name = _data.name
        data.email = _data.email
        data.username = _data.username
        data.phone_number = _data.phone_number
        return data

    def GetUserList(self, request, context):
        _datas = UserDB().get_user()
        _user_data = data_stream_service_pb2.UserDataList()
        for _data in _datas:
            data = data_stream_service_pb2.UserData()
            data.name = _data.name
            data.email = _data.email
            data.username = _data.username
            data.phone_number = _data.phone_number
            _user_data.list.append(data)
        return _user_data


class GrpcServer:
    def __init__(self, host='0.0.0.0', port='50051', max_workers=10):
        self.host = host
        self.port = port
        self.max_workers = max_workers

    def serve(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=self.max_workers))
        data_stream_service_pb2_grpc.add_DataStreamServicer_to_server(UserDataServicer(), server)
        server.add_insecure_port(f"{self.host}:{self.port}")
        server.start()
        print(f'Server started at {self.host}:{self.port}')
        server.wait_for_termination()

if __name__ == "__main__":
    GrpcServer().serve()
