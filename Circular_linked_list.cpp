#include <iostream>
#include <vector>
using namespace std;

// SinglyLinked list
struct Node {
  int value;
  Node *next = nullptr;
  Node(){};
  Node(int value) : value(value) {}
  Node(int value, Node *next) : value(value), next(next) {}
};

class CircLinkedList {
private:
  Node *head = nullptr;
  int size = 0;

  Node *get_node(int index) {
    Node *current = head;
    int current_index = 0;
    if (size == 0) {
      throw out_of_range("List cannot be empty");
    }
    while (current != nullptr) {
      if (index == current_index) {
        return current;
      }
      current = current->next;
      current_index++;
    }
    return current;
  }

public:
  CircLinkedList() {}
  CircLinkedList(int n) {
    for (int i = 1; i < n + 2; i++)
      append(i);
  }
  ~CircLinkedList() {
    Node *current = head;
    Node *next = head;
    while (current != nullptr) {
      next = current->next;
      delete current;
      current = next;
    }
  }

  // 2. Append a node to the list
  void append(int value) {
    Node *new_node = new Node(value);
    if (head == nullptr) {
      head = new_node;
      return;
    } else {
      Node *current = head;
      while (current->next != nullptr) {
        current = current->next;
      }
      current->next = new_node;
    }
    size++;
  }

  int &operator[](int index) {
    Node *node = get_node(index);
    return node->value;
  }
  void print() {
    cout << "[ ";
    Node *current = head;
    for (int i = 0; i < size + 1; i++) {
      cout << current->value << " ";
      current = current->next;
    }
    cout << "]\n";
  }

  vector<int> josephus_sequence(int k) {
    Node *temp;
    Node *head;
    vector<int> data;
    int n = size;
    // creating a temporary copy of the input node
    head = new Node;
    temp = head;
    temp->value = 1;
    for (int i = 2; i <= n; ++i) {
      temp->next = new Node;
      temp = temp->next;
      temp->value = i;
    }
    temp->next = head;
    // Process of deletion
    for (int count = n; count > 1; --count) {
      for (int i = 1; i < k; ++i) {
        temp = temp->next;
      }
      Node *q = temp->next;
      data.push_back(q->value);
      temp->next = temp->next->next;
      delete q;
    }
    // adding the final result
    data.push_back(temp->value);
    return data;
  }
};

int last_man_standing(int n, int k) {
  CircLinkedList cll{n};
  vector<int> data = cll.josephus_sequence(k);
  return data[data.size() - 1];
}
int main() {
  cout << last_man_standing(67, 7) << endl;
/*
  CircLinkedList clist;
  clist.append(0);
  clist.append(2);
  clist.append(4);
  clist.append(7);
  cout << clist[3] << endl;
  clist.print();
  */

  


  return 0;
}
