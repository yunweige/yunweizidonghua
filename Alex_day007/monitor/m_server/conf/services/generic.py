class DefaultService:
    name = 'DefaultService'
    interval = 300
    plugin_name = None
    index_dic = None
    triggers = {}
    data_from = 'agent'
    graph_index = {
        'index' :[],
        'title' : name,
    }
    lt_operator = []