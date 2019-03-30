```scs
sc_type
    -> sc_const;
    -> sc_var;
    
    -> sc_node;
    -> sc_link;
    -> sc_edge_dcommon;
    -> sc_edge_ucommon;
    -> sc_edge_main;
    -> sc_edge_access;

    // edge types
    -> sc_edge_pos;
    -> sc_edge_neg;
    -> sc_edge_fuz;
    -> sc_edge_perm;
    -> sc_edge_temp;
    
    -> sc_node_not_binary_tuple;
    -> sc_node_struct;
    -> sc_node_role_relation;
    -> sc_node_norole_relation;
    -> sc_node_not_relation; // deprecated: use sc_node_class instead
    -> sc_node_class;
    -> sc_node_abstract;
    -> sc_node_material;;
```