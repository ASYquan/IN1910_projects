#include <cassert>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;

struct Node {
  int value;
  Node *next;
  Node *prev;

  Node(int val) {
    value = val;
    next = nullptr;
    prev = nullptr;
  }
  Node(int value, Node *next) : value(value), next(next) {}
};

class LinkedList {
private:
  Node *head;
  Node *tail;
  Node *get_node(int index) {
    Node *current = head;
    int current_index = 0;
    while (current != nullptr) {
      if (index == current_index) {
        return current;
      }
      current = current->next;
      current_index++;
    }
    throw out_of_range("index " + to_string(index) + "is out of bounds");
  }

public:
  LinkedList() {
    head = nullptr;
    tail = nullptr;
  }
  LinkedList(vector<int> init) {
    head = nullptr;
    tail = nullptr;
    for (int e : init) {
      append(e);
    }
  }
  ~LinkedList() {
    Node *current = head;
    Node *next = head;
    while (current != nullptr) {
      next = current->next;
      delete current;
      current = next;
    }
  }

  int length() {
    int length = 0;
    Node *current = head;
    while (current != nullptr) {
      current = current->next;
      length++;
    }
    return length;
  }

  void append(int value) {
    Node *new_node = new Node(value);
    if (head == nullptr) {
      head = new_node;
    }
    if (tail == nullptr) {
      tail = new_node;
    } else {
      tail->next = new_node;
      tail = new_node;
    }
  }
  void print() {
    cout << "[ ";
    Node *current = head;
    while (current != nullptr) {
      cout << current->value << " ";
      current = current->next;
    }
    cout << "]\n";
  }
  int &operator[](int index) {
    Node *node = get_node(index);
    return node->value;
  }
  void insert(int val, int index) {
    if (index == 0) {
      head = new Node(val, head);

    } else if (index == length()) {
      append(val);
    } else if (head != nullptr) {
      Node *prev = get_node(index - 1);
      Node *next = prev->next;
      prev->next = new Node(val, next);
    }
  }
  void remove(int index) {
    int n = index + 1;
    Node *temp1 = head;
    if (head->next == nullptr) {
      delete head;
      head = nullptr;
      tail = nullptr;
    } else if (n == 1) {
      head = head->next;
      delete head->prev;
      head->prev = nullptr;
    } else if (head != nullptr) {
      for (int i = 0; i < n - 2; i++) {
        temp1 = temp1->next;
      }
      Node *temp2 = temp1->next;
      temp1->next = temp2->next;
      delete temp2;
    }
  }
  int pop(int index) {
    Node *node = get_node(index);
    int val = node->value;
    remove(index);
    return val;
  }
  int pop() {
    Node *node = get_node(length() - 1);
    int val = node->value;
    remove(length() - 1);
    return val;
  }
};

int main() {
  cout << "For testing, we will use two objects of LinkedList-class: " << endl;
  cout << "empty_list, will be an object of no input" << endl;
  cout << "data_list, will be an object with vector as input" << endl;

  cout << "\n";
  LinkedList empty_list{};
  vector<int> data = {1, 2, 3, 4, 5, 6};
  LinkedList data_list{data};
  cout << "data_list: " << endl;
  data_list.print();
  cout << "empty:list: " << endl;
  empty_list.print();
  cout << "\n";

  int i = 0;
  while (empty_list.length() < 10) {
    empty_list.append(i);
    i++;
  }
  cout << "empty_list, after use of append: " << endl;
  empty_list.print();
  cout << "data_list, after use of append: " << endl;
  data_list.append(7);
  data_list.print();

  cout << "Length of empty_list: " << empty_list.length() << endl;
  cout << "Length of data_list: " << data_list.length() << endl;
  cout << "\n";
  cout << "empty_list[3] = " << empty_list[3] << endl;
  cout << "data_list[3] = " << data_list[3] << endl;
  cout << "\n";
  empty_list.remove(0);
  data_list.remove(0);
  cout << "Removing the first element of both objects: " << endl;
  empty_list.print();
  data_list.print();
  cout << "\n";
  cout << "Using pop with argument for both objects: " << endl;
  cout << "empty_list.pop(4) : " << empty_list.pop(4) << endl;
  cout << "data_list.pop(4) : " << data_list.pop(4) << endl;
  empty_list.print();
  data_list.print();
  cout << "\n";
  cout << "Using pop without argument for both objects: " << endl;
  cout << "empty_list.pop(): " << empty_list.pop() << endl;
  cout << "data_list.pop(): " << data_list.pop() << endl;
  empty_list.print();
  data_list.print();
  cout << "\n";

  cout << "Destructor test: " << endl;
  cout << "We will test the destructor by creating a scope. In the destructor "
       << endl;
  cout << "In our scope we will create a new LinkedList. If we try to call "
          "upon the list outside of the scope, we should get an error message "
          "saying it doesnt exist."
       << endl;
  {
    vector<int> temp = {1, 2, 3};
    LinkedList ll{temp};
    cout << "Calling our temporaryly created class-object:" << endl;
    cout << "printing class object: ";
    ll.print();
  }
  cout << "If we use an external tool such as valgrind we will se that it has "
          "been dallocated"
       << endl;

  return 0;
}
