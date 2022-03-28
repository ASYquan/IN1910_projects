#include <cassert>
#include <chrono>    // for high_resolution_clock
#include <fstream>   // for ofstream
#include <iostream>  // for cout
#include <stdexcept> // for runtime_error
#include <vector>    // for vector (exercise 1f)

using namespace std::chrono;
using namespace std;

class ArrayList {
private:
  int *data;
  int capacity = 1;
  int size = 0;

  void resize() {
    capacity *= 2;
    int *tmp = new int[capacity];
    for (int i = 0; i < size; i++) {
      tmp[i] = data[i];
    }
    delete[] data;
    data = tmp;
  }

public:
  int cap() { return capacity; }
  ArrayList() { data = new int[capacity]; }
  int length() { return size; }
  ~ArrayList() { delete[] data; }
  ArrayList(vector<int> init) {
    size = 0;
    capacity = 1;
    data = new int[capacity];

    for (int e : init) {
      append(e);
    }
  }
  void append(int n) {
    if (size >= capacity) {
      resize();
    }
    data[size] = n;
    size += 1;
  }
  void print() {
    cout << "[";
    for (int i = 0; i < size - 1; i++) {
      cout << data[i] << ", ";
    }
    cout << data[size - 1] << "]\n";
  }
  int &operator[](int i) {
    if (0 <= i and i < size) {
      return data[i];
    } else {
      throw out_of_range("IndexError");
    }
  }
  void insert(int val, int index) {
    if (index > size || index < 0) {
      throw out_of_range("IndexError");
    }
    if (index == size) {
      append(val);
    } else if (index != size) {
      size++;
      if (size >= capacity) {
        resize();
      }
      for (int i = size; i >= index; i--) {
        data[i] = data[i - 1];
      }
      data[index] = val;
      if (length() < capacity * 0.25) {
        shrink_to_fit();
      }
    }
  }
  void remove(int index) {
    for (int i = index; i < size; i++) {
      data[i] = data[i + 1];
      cout << "data: " << data[i] << endl;
    }
    if (size < capacity * 0.25) {
      shrink_to_fit();
    }
  }

  int pop(int index) {
    int val = data[index];
    remove(index);
    return val;
  }
  int pop() {
    int val = data[size];
    remove(size);
    return val;
  }
  void shrink_to_fit() {
    int n = 1;
    while (n < size) {
      n *= 2;
    }
    capacity = n;
  }
};

bool is_prime(int n) {
  bool statement = true;
  for (int i = 2; i <= n / 2; i++) {
    if (n % i == 0) {
      statement = false;
      break;
    }
  }
  return statement;
}

void test_append_arr() {
  ArrayList arr{};
  int i = 0;
  while (arr.length() < 10) {
    if (is_prime(i) == true) {
      arr.append(i);
    }
    i++;
  }
  arr.print();
}

void test_shrink_to_fit() {
  /*Tar utgangspunkt i oppgaven som sier at en arary med lengde 47
  burde ha capacity på 64. Lagde også en public-metode som henter capacity */
  ArrayList arr{};
  for (int i = 0; i < 47; i++) {
    arr.append(i);
  }
  int exp_cap = 64;
  int comp_cap = arr.cap();
  assert((exp_cap == comp_cap));
}

int main() {
  test_append_arr();
  test_shrink_to_fit();
  return 0;
}
