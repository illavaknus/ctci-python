from LinkedList import LinkedList

def remove_dups(linked_list):
    if len(linked_list) < 2:
        return linked_list
    else:
        p = linked_list.head
        elems = set(str(p))
        
        while p.next is not None:
            if str(p.next) in elems:
                p.next = p.next.next
            else:
                elems.add(str(p.next))
                p = p.next
        return linked_list

def remove_dups_followup(linked_list):
    if len(linked_list) < 2:
        return linked_list
    else:
        cur = linked_list.head
        while cur is not None:
            p = cur
            while p.next is not None:
                if str(p.next) == str(cur):
                    p.next = p.next.next
                else:
                    p = p.next
            cur = cur.next
        return linked_list

if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(50,1,10)
    print(ll)
    remove_dups(ll)
    print(ll,len(ll))

    ll2 = LinkedList()
    ll2.generate(50,1,10)
    print(ll2)
    remove_dups_followup(ll2)
    print(ll2,len(ll2))