```scs
// append set of apples into fruit set
sc_node#fruit | sc_edge_main#edge | sc_node#apple;;
// append set of bananas into fruit set
sc_node#fruit | sc_edge_main#... | sc_node#banana;;

sc_node#apple | sc_edge_dcommon#..e | "file://apple.png";;
/*append edge from nrel_image relation into
  edge between apple set and it's image*/
sc_node#nrel_image | sc_edge_main#... | sc_edge_dcommon#..e;;
```