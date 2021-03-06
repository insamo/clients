# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: auth/auth.proto for package 'go.micro.auth'

require 'grpc'
require 'auth/auth_pb'

module Go
  module Micro
    module Auth
      module Auth
        class Service

          include GRPC::GenericService

          self.marshal_class_method = :encode
          self.unmarshal_class_method = :decode
          self.service_name = 'go.micro.auth.Auth'

          rpc :Generate, Go::Micro::Auth::GenerateRequest, Go::Micro::Auth::GenerateResponse
          rpc :Inspect, Go::Micro::Auth::InspectRequest, Go::Micro::Auth::InspectResponse
          rpc :Token, Go::Micro::Auth::TokenRequest, Go::Micro::Auth::TokenResponse
        end

        Stub = Service.rpc_stub_class
      end
      module Accounts
        class Service

          include GRPC::GenericService

          self.marshal_class_method = :encode
          self.unmarshal_class_method = :decode
          self.service_name = 'go.micro.auth.Accounts'

          rpc :List, Go::Micro::Auth::ListAccountsRequest, Go::Micro::Auth::ListAccountsResponse
        end

        Stub = Service.rpc_stub_class
      end
      module Rules
        class Service

          include GRPC::GenericService

          self.marshal_class_method = :encode
          self.unmarshal_class_method = :decode
          self.service_name = 'go.micro.auth.Rules'

          rpc :Create, Go::Micro::Auth::CreateRequest, Go::Micro::Auth::CreateResponse
          rpc :Delete, Go::Micro::Auth::DeleteRequest, Go::Micro::Auth::DeleteResponse
          rpc :List, Go::Micro::Auth::ListRequest, Go::Micro::Auth::ListResponse
        end

        Stub = Service.rpc_stub_class
      end
    end
  end
end
