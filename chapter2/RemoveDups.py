from LinkedList import LinkedList

def remove_dups(linked_list):

    if len(linked_list) < 2:
        return linked_list
    else:
        p = linked_list.head
        elems = set(str(p))
        
        while p is not None and p.next is not None:
            if str(p.next) in elems:
                p.next = p.next.next
            else:
                elems.add(str(p.next))
                p = p.next
        return linked_list

if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(20,1,10)
    print(ll)
    print(remove_dups(ll))