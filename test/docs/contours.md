```scs
fix -> [*
	begin -> test;;
	end -> [test content];;
*];;

cmd
=> nrel_common_template:
        [*
            command_list_set
                _-> _command;;
                
            _command
                _-> rrel_1:: _set; // There is a problem
        *];;

_command
    _-> rrel_1:: _set;
```