# Generated by the protocol buffer compiler.  DO NOT EDIT!
# Source: network/network.proto for package 'go.micro.network'

require 'grpc'
require 'network/network_pb'

module Go
  module Micro
    module Network
      module Network
        # Network service is usesd to gain visibility into networks
        class Service

          include GRPC::GenericService

          self.marshal_class_method = :encode
          self.unmarshal_class_method = :decode
          self.service_name = 'go.micro.network.Network'

          # Connect to the network
          rpc :Connect, Go::Micro::Network::ConnectRequest, Go::Micro::Network::ConnectResponse
          # Returns the entire network graph
          rpc :Graph, Go::Micro::Network::GraphRequest, Go::Micro::Network::GraphResponse
          # Returns a list of known nodes in the network
          rpc :Nodes, Go::Micro::Network::NodesRequest, Go::Micro::Network::NodesResponse
          # Returns a list of known routes in the network
          rpc :Routes, Go::Micro::Network::RoutesRequest, Go::Micro::Network::RoutesResponse
          # Returns a list of known services based on routes
          rpc :Services, Go::Micro::Network::ServicesRequest, Go::Micro::Network::ServicesResponse
          # Status returns network status
          rpc :Status, Go::Micro::Network::StatusRequest, Go::Micro::Network::StatusResponse
        end

        Stub = Service.rpc_stub_class
      end
    end
  end
end
