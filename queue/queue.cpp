#include<iostream>

using namespace std;

class Queue{
    int front, rear, capacity;
    int *arr;

    public:
        Queue(int);
        void enqueue(int);
        int dequeue();
        int peek();
        bool isEmpty();
        bool isFull();
};

Queue::Queue(int capacity){
    front = -1;
    rear = -1;
    capacity = capacity;
    arr = new int[capacity];
}

bool Queue::isEmpty(){
    return front==-1 && rear==-1;
}

bool Queue::isFull(){
    return (rear-front)+1 == capacity;
}

void Queue::enqueue(int data){
    if (isFull()) {
        cout << "Queue is full." << endl;
        exit(EXIT_FAILURE);
    }else{
        if (isEmpty()){
            front++;
        }

        rear++;
        arr[rear] = data;
        cout << data << " inserted successfully." << endl;
    }
}

int Queue::dequeue(){
    int data = 0;
    if (isEmpty()){
        cout << "Queue is empty." << endl;
        exit(EXIT_FAILURE);
    }else{
        data = arr[front];
        front++;
        cout << data << " removed successfully." << endl;

        if (front > rear){
            front = -1;
            rear = -1;
        }
    }

    return data;
}

int Queue::peek(){
    int data = 0;
    if (isEmpty()){
        cout << "Queue is empty." << endl;
        exit(EXIT_FAILURE);
    }else{
        data = arr[front];
    }

    return data;
}

int main(){
    Queue q(10);

    q.enqueue(10);

    q.dequeue();

    return 0;
}