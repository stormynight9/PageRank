def pagerank(graph):
    # Initialize values for all nodes s.t. that add up to one
    n = len(graph.nodes)
    init_val = 1.0/n
    ranks = dict(zip(graph.get_nodes(), [init_val] * n))

    new_ranks = ranks
    for node, value in new_ranks.items():
        print(node.name, value)
    print('-----------')

    # Calculate new rank for each node
    for node, prev_rank in ranks.items():
        rank_sum = 0.0

        # Iterate through incoming nodes
        for incoming_node in node.inbound:
            numerator = ranks[incoming_node]
            denominator = len(incoming_node.outbound)
            transfer_amount = numerator / denominator

            # Transfer rank score
            new_ranks[incoming_node] = new_ranks[incoming_node] - \
                transfer_amount
            rank_sum = rank_sum + transfer_amount

        new_ranks[node] = ranks[node] + rank_sum
        for node, value in new_ranks.items():
            print(node.name, value)
        print('-----------')

    # Set ranks to the new ranks calculated in this iteration
    ranks = new_ranks

    return ranks
