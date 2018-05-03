#include<iostream>
using namespace std;

struct node{
    int key;
    node *left;
    node *right;
};
node* createNode(int data ){
    node *temp=new node;
    temp->key=data;
    temp->left=nullptr;
    temp->right=nullptr;
    return temp;
}
int main(){
    node *root=createNode(1);
    return 0;}