import ipaddress


def available_subnets(cidr_block: str,
                      public_subnets_count: int,
                      private_subnets_count: int) -> (list, list):
    network = ipaddress.ip_network(cidr_block)

    subnet_mask = network.prefixlen + max(public_subnets_count, private_subnets_count)

    total_cidr_blocks = list(network.subnets(new_prefix=subnet_mask))

    public_subnets = total_cidr_blocks[:public_subnets_count]
    private_subnets = total_cidr_blocks[public_subnets_count:public_subnets_count + private_subnets_count]

    return public_subnets, private_subnets
