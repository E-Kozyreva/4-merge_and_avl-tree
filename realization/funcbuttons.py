class ShowButtons:
    def merge_algo(t_way, f_way, e_way, back):
        t_way.show()
        f_way.show()
        e_way.show()
        back.show()
        return t_way, f_way, e_way, back

    def merge_algo_back(merge, tree, exit):
        merge.show()
        tree.show()
        exit.show()
        return merge, tree, exit
    
    def tree_algo(avl, back):
        avl.show()
        back.show()
        return avl, back

    def tree_algo_back(merge, tree, exit):
        merge.show()
        tree.show()
        exit.show()
        return merge, tree, exit


class HideButtons:
    def merge_algo(merge, tree, exit):
        merge.hide()
        tree.hide()
        exit.hide()
        return merge, tree, exit

    def merge_algo_back(t_way, f_way, e_way, back):
        t_way.hide()
        f_way.hide()
        e_way.hide()
        back.hide()
        return t_way, f_way, e_way, back
    
    def tree_algo(merge, tree, exit):
        merge.hide()
        tree.hide()
        exit.hide()
        return merge, tree, exit
    
    def tree_algo_back(avl, back):
        avl.hide()
        back.hide()
        return avl, back