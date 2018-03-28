# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


def run():
    creds = grpc.ssl_channel_credentials(root_certificates=open("certs/CAcert.pem").read(),
                                         private_key=open("certs/client.pem").read(),
                                         certificate_chain=open("certs/client.crt").read())

    session_cache = grpc.ssl_session_cache(1024)
    options = [('grpc.ssl_target_name_override', 'server'),
               ('grpc.ssl_session_cache', session_cache)]

    channel = grpc.secure_channel('localhost:50051', creds, options=options)
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)

    channel = grpc.secure_channel('localhost:50051', creds, options=options)
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
