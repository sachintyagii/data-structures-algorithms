#include <iostream>
#define MAX 100

using namespace std;

class Node{
  public:
    int value;
    int priority;
};

class PriorityQueue{
  private:
    Node queue[MAX];
    int size;
  public:
    PriorityQueue();
    void enqueue(int, int);
    int dequeue();
    int peek();
    int getQueueValue(int);
    void display();
};

PriorityQueue::PriorityQueue(){
  Node queue[MAX];
  size=-1;
}

int PriorityQueue::peek(){
  int maxPriority = queue[0].priority;
  int index = 0;

  for (int i=1; i<=size; i++){
    if(maxPriority < queue[i].priority){
      maxPriority = queue[i].priority;
      index = i;
    }
  }

  return index;
}

int PriorityQueue::getQueueValue(int index){
  return queue[index].value;
}

void PriorityQueue::enqueue(int data, int priority){
  size++;
  queue[size].value = data;
  queue[size].priority = priority;
}

int PriorityQueue::dequeue(){
  int index = peek();

  for(int i=index; i<=size; i++){
    queue[i] = queue[i+1];
  }
  size--;

  return index;
}

void PriorityQueue::display(){
  cout << "******************" << endl;
  for (int i=0; i<=size; i++){
    cout << queue[i].value << ", " << queue[i].priority << endl;
  }
}

int main() {
  PriorityQueue pq;
  int idx;

  pq.enqueue(100, 10);
  pq.enqueue(200, 9);
  pq.enqueue(300, 10);
  pq.display();
  pq.dequeue();
  pq.display();
  
  return 0;
}
