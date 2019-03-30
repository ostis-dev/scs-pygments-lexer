```scs
scp_program -> proc_find_carcass (*

	-> rrel_params: ... (*
		-> rrel_1: rrel_in: _graph;;
		-> rrel_2: rrel_in: _root_vertex;;

		-> rrel_3: rrel_out: _carcass;;
	*);;

	-> rrel_operators: ... (*
	
	-> rrel_init: ..proc_find_carcass_create_carcass (*
		<- genEl;;
		-> rrel_1: rrel_assign: rrel_const: rrel_node: rrel_scp_var: _carcass;;

		=> nrel_goto: ..proc_find_carcass_create_unchecked_vertexes;;
		*);;

// Добавление всех вершин во множество непроверенных вершин.	
	-> ..proc_find_carcass_create_unchecked_vertexes (*
		<- searchSetStr5;;
		-> rrel_1: rrel_fixed: rrel_scp_var: _graph;;
		-> rrel_2: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc2;;
		-> rrel_3: rrel_assign: rrel_scp_var: _el3;;
		-> rrel_4: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc4;;
		-> rrel_5: rrel_fixed: rrel_scp_const: rrel_vertex;;
		
		-> rrel_set_3: rrel_assign: rrel_scp_var: _not_checked_vertexes;; // множество непроверенных вершин

		=> nrel_then: ..proc_find_carcass_create_queue_front;;		
		=> nrel_else: ..proc_find_carcass_erase_unchecked_vertexes;;
	*);;

// Создание очереди
-> ..proc_find_carcass_create_queue_front (*
		<- genEl;;
		-> rrel_1: rrel_assign: rrel_const: rrel_node: rrel_scp_var: _queue_front;;

		=> nrel_goto: ..proc_find_carcass_create_queue_back;;
		*);;

-> ..proc_find_carcass_create_queue_back (*
		<- genEl;;
		-> rrel_1: rrel_assign: rrel_const: rrel_node: rrel_scp_var: _queue_back;;

		=> nrel_goto: ..proc_find_carcass_find_root_vertex;;
		*);;
//

// Находим корневую вершину дерева во множестве непроверенных вершин.
	-> ..proc_find_carcass_find_root_vertex (*
		<- searchElStr3;;
		-> rrel_1: rrel_fixed: rrel_scp_var: rrel_node: _not_checked_vertexes;;
		-> rrel_2: rrel_assign: rrel_scp_var: rrel_pos_const_perm: _arc2;;
		-> rrel_3: rrel_fixed: rrel_scp_var: rrel_node: _root_vertex;;

		 => nrel_then: ..proc_find_carcass_delete_root_vertex;;	
	*);;
		
// Удаляем корневую вершину из множества непроверенных вершин.
	-> ..proc_find_carcass_delete_root_vertex (*
		<- eraseEl;;
		 -> rrel_1: rrel_fixed: rrel_erase: rrel_scp_var: _arc2;;

		 => nrel_goto: /* test */..proc_find_carcass_queue_add_root_vertex;;	
	*);;

//  Добавляем в очередь корневую вершину. От неё будет начинаться поиск
//---------------------------------------------------------------------
	-> ..proc_find_carcass_queue_add_root_vertex (*
		<- call;;
		-> rrel_1: rrel_fixed: rrel_scp_const: proc_queue_add;;
		-> rrel_2: rrel_fixed: rrel_scp_const: ... (*
			-> rrel_1: rrel_fixed: rrel_scp_var: _queue_front;;
			-> rrel_2: rrel_fixed: rrel_scp_var: _queue_back;;
			-> rrel_3: rrel_fixed: rrel_scp_var: _root_vertex;;
		*);;
		-> rrel_3: rrel_assign: rrel_scp_var: _descr;;

		=> nrel_goto: ..proc_find_carcass_queue_add_root_vertex_return;;
	*);;

	-> ..proc_find_carcass_queue_add_root_vertex_return (*
		<- waitReturn;;
		-> rrel_1: rrel_fixed: rrel_scp_var: _descr;;

		=> nrel_goto: ..proc_find_carcass_add_root_vertex;;
	*);;

//  Добавляем корневую вершину в каркас.
	-> ..proc_find_carcass_add_root_vertex (*
		<- genElStr5;;
		-> rrel_1: rrel_fixed: rrel_node: rrel_scp_var: _carcass;;
		-> rrel_2: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc2;;
		-> rrel_3: rrel_fixed: rrel_node: rrel_scp_var: _root_vertex;;
		-> rrel_4: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc4;;
		-> rrel_5: rrel_fixed: rrel_scp_const: rrel_vertex;;

		=> nrel_goto: ..proc_find_carcass_main_loop_start;;
	*);;

//! обход графа в ширину.

// Проверяем, пустая ли очередь.
	-> ..proc_find_carcass_main_loop_start (*
		<- searchElStr3;;
		-> rrel_1: rrel_fixed: rrel_scp_var: rrel_node: _queue_front;;
		-> rrel_2: rrel_assign: rrel_scp_var: rrel_pos_const_perm: _arc2;;
		-> rrel_3: rrel_assign: rrel_scp_var: rrel_node: _queue_element;;

		 => nrel_then: ..proc_find_carcass_queue_pop;; // если очередь не пустая
		 => nrel_else: ..proc_find_carcass_check_unchecked_vertexes;; // если очередь пустая
	*);;

// Извлекаем вершину из очереди.
	-> ..proc_find_carcass_queue_pop (*
		<- call;;
		-> rrel_1: rrel_fixed: rrel_scp_const: proc_queue_pop;;
		-> rrel_2: rrel_fixed: rrel_scp_const: ... (*
			-> rrel_1: rrel_fixed: rrel_scp_var: _queue_front;;
			-> rrel_2: rrel_fixed: rrel_scp_var: _queue_back;;
			-> rrel_3: rrel_assign: rrel_scp_var: _current_vertex;;
		*);;
		-> rrel_3: rrel_assign: rrel_scp_var: _descr;;

		=> nrel_goto: ..proc_find_carcass_queue_pop_return;;
	*);;

	-> ..proc_find_carcass_queue_pop_return (*
		<- waitReturn;;
		-> rrel_1: rrel_fixed: rrel_scp_var: _descr;;

		=> nrel_goto: ..proc_find_carcass_create_edges_set;;
	*);;

// Создание множества всех рёбер графа для поиска смежных вершин.	
	-> ..proc_find_carcass_create_edges_set (*
		<- searchSetStr5;;
		-> rrel_1: rrel_fixed: rrel_scp_var: _graph;;
		-> rrel_2: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc2;;
		-> rrel_3: rrel_assign: rrel_scp_var: _edge;;
		-> rrel_4: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc4;;
		-> rrel_5: rrel_fixed: rrel_scp_const: rrel_edge;;
		
		-> rrel_set_3: rrel_assign: rrel_scp_var: _graph_edges_set;; // множество ребер графа

		=> nrel_then: ..proc_find_carcass_find_adjacent_vertex;;
		=> nrel_else: ..proc_find_carcass_erase_unchecked_vertexes;;
	*);;

// Цикл поиска вершин, смежных вершине _current_vertex
	-> ..proc_find_carcass_find_adjacent_vertex (*
		<- searchElStr5;;
		-> rrel_1: rrel_fixed: rrel_scp_var: rrel_node: _current_vertex;;
		-> rrel_2: rrel_assign: rrel_scp_var: _adjacent_vertex_edge;; // ребро, соединяющее текущую вершину со смежной
		-> rrel_3: rrel_assign: rrel_scp_var: rrel_node: _adjacent_vertex;; // смежная вершина
		-> rrel_4: rrel_assign: rrel_scp_var: rrel_pos_const_perm: _arc4;;
		-> rrel_5: rrel_fixed: rrel_scp_var: rrel_node: _graph_edges_set;;

		 => nrel_then: ..proc_find_carcass_delete_adjacent_vertex_edge;; // смежная вершина найдена
		 => nrel_else: ..proc_find_carcass_main_loop_start;; // смежных вершин больше нет
	*);;

// Удаляем пройденное ребро из множества всех ребер
	-> ..proc_find_carcass_delete_adjacent_vertex_edge (*
			<- eraseEl;;
			-> rrel_1: rrel_fixed: rrel_scp_var: rrel_erase: _arc4;;

			=> nrel_goto: ..proc_find_carcass_adjacent_vertex_is_unchecked;;
		*);;

// Проверка на принадлежность смежной вершины множеству непроверенных вершин
	-> ..proc_find_carcass_adjacent_vertex_is_unchecked (*
		<- searchElStr3;;
		-> rrel_1: rrel_fixed: rrel_scp_var: rrel_node: _not_checked_vertexes;;
		-> rrel_2: rrel_assign: rrel_scp_var: rrel_pos_const_perm: _arc2;;
		-> rrel_3: rrel_fixed: rrel_scp_var: rrel_node: _adjacent_vertex;;

		 => nrel_then: ..proc_find_carcass_delete_adjacent_vertex;; // смежная вершина ещё не была проверена, работаем с ней
		 => nrel_else: ..proc_find_carcass_find_adjacent_vertex;; // смежная вершина уже посещена, ищем другую
	*);;

// Удаляем смежную вершину из множества непроверенных вершин
	-> ..proc_find_carcass_delete_adjacent_vertex (*
			<- eraseEl;;
			-> rrel_1: rrel_fixed: rrel_scp_var: rrel_erase: _arc2;;

			=> nrel_goto: ..proc_find_carcass_queue_add_adjacent_vertex;;
		*);;

//  Добавляем в очередь смежную вершину.
//-------------------------------------------------------------------
	-> ..proc_find_carcass_queue_add_adjacent_vertex (*
		<- call;;
		-> rrel_1: rrel_fixed: rrel_scp_const: proc_queue_add;;
		-> rrel_2: rrel_fixed: rrel_scp_const: ... (*
			-> rrel_1: rrel_fixed: rrel_scp_var: _queue_front;;
			-> rrel_2: rrel_fixed: rrel_scp_var: _queue_back;;
			-> rrel_3: rrel_fixed: rrel_scp_var: _adjacent_vertex;;
		*);;
		-> rrel_3: rrel_assign: rrel_scp_var: _descr;;

		=> nrel_goto: ..proc_find_carcass_queue_add_adjacent_vertex_return;;
	*);;

	-> ..proc_find_carcass_queue_add_adjacent_vertex_return (*
		<- waitReturn;;
		-> rrel_1: rrel_fixed: rrel_scp_var: _descr;;

		=> nrel_goto: ..proc_find_carcass_add_adjacent_vertex;;
	*);;

//  Добавляем смежную вершину в каркас.
	-> ..proc_find_carcass_add_adjacent_vertex (*
		<- genElStr5;;
		-> rrel_1: rrel_fixed: rrel_node: rrel_scp_var: _carcass;;
		-> rrel_2: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc2;;
		-> rrel_3: rrel_fixed: rrel_node: rrel_scp_var: _adjacent_vertex;;
		-> rrel_4: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc4;;
		-> rrel_5: rrel_fixed: rrel_scp_const: rrel_vertex;;

		=> nrel_goto: ..proc_find_carcass_add_adjacent_vertex_edge;;
	*);;

//  Добавляем ребро к смежной вершине в каркас.
	-> ..proc_find_carcass_add_adjacent_vertex_edge (*
		<- genElStr5;;
		-> rrel_1: rrel_fixed: rrel_node: rrel_scp_var: _carcass;;
		-> rrel_2: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc2;;
		-> rrel_3: rrel_fixed: rrel_scp_var: _adjacent_vertex_edge;;
		-> rrel_4: rrel_assign: rrel_pos_const_perm: rrel_scp_var: _arc4;;
		-> rrel_5: rrel_fixed: rrel_scp_const: rrel_edge;;

		=> nrel_goto: ..proc_find_carcass_find_adjacent_vertex;;
	*);;

// Проверим, пустое ли множество непроверенных вершин
	-> ..proc_find_carcass_check_unchecked_vertexes (*
		<- searchElStr3;;
		-> rrel_1: rrel_fixed: rrel_scp_var: _not_checked_vertexes;;
		-> rrel_2: rrel_assign: rrel_scp_var: _arc2;;
		-> rrel_3: rrel_assign: rrel_scp_var: _random_vert;;

		=> nrel_then: ..proc_find_carcass_erase_carcass;; // eсли оно не пустое
		=> nrel_else: ..proc_find_carcass_erase_unchecked_vertexes;; // если пустое
	*);;

// Если какие-то вершины остались непосещенными, каркас построить нельзя
	-> ..proc_find_carcass_erase_carcass (*
		<- eraseEl;;
		-> rrel_1: rrel_fixed: rrel_scp_var: rrel_erase: _carcass;;

		=> nrel_goto: ..proc_find_carcass_erase_unchecked_vertexes;;
	*);;

// Удаление множества непосещенных вершин
	-> ..proc_find_carcass_erase_unchecked_vertexes (*
		<- eraseEl;;
		-> rrel_1: rrel_fixed: rrel_scp_var: rrel_erase: _not_checked_vertexes;;

		=> nrel_goto: ..proc_carcass_return;;
	*);;

// Выход из программы
	-> ..proc_carcass_return (*
		<- return;;
	*);;

	*);;
*);;
```