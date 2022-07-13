#include <iostream>
#define MAX 100

using namespace std;

class Stack{
    private:
        int top;
        int capacity;
        int *arr;
    public:
        Stack(int capacity=MAX);
        void push(int);
        int pop();
        bool isEmpty();
        bool isFull();
        int peek();
        int size();
        void display();
};

Stack::Stack(int capacity){
    top = -1;
    capacity = capacity;
    arr = new int[capacity];
}

bool Stack::isEmpty(){
    return top == -1;
}

int Stack::size(){
    return top+1;
}

bool Stack::isFull(){
    return size()==capacity;
}

void Stack::push(int data){
    if (isFull()){
        cout<<"Stack Overflow"<<endl;
        exit(EXIT_FAILURE);
    }else{
        cout<<"Inserting: "<<data<<endl;
        top++;
        arr[top] = data;
    }
}

int Stack::pop(){
    int data=0;
    if(isEmpty()){
        cout<<"Stack Underflow"<<endl;
        exit(EXIT_FAILURE);
    }else{
        data = arr[top];
        top--;
        cout<<"Deleting: "<<data<<endl;
    }
    return data;
}

int Stack::peek(){
    int data=0;
    if(isEmpty()){
        cout<<"Stack Underflow"<<endl;
        exit(EXIT_FAILURE);
    }else{
        data = arr[top];
    }
    return data;
}

void Stack::display(){
    if(isEmpty()){
        cout<<"Stack Underflow"<<endl;
        exit(EXIT_FAILURE);
    }else{
        cout<<"Top: "<<top<<endl;
        for(int i=0; i<=top; i++){
            cout<<arr[i]<<endl;
        }
    }
}

int main(){
    Stack stack(10);
    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);
    stack.display();

    stack.pop();
    stack.display();
}