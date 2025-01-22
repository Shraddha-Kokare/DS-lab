//============================================================================
// Name        : Dictionary.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style

//A dictionary stores keywords and its meanings.
//Provide facility for adding new keywords, deleting keywords, updating values of any entry.
//Provide facility to display whole data sorted in ascending/ Descending order.
//Also find how many maximum comparisons may require for finding any keyword.
//Use Binary Search Tree for implementation.

//============================================================================

#include <iostream>
#include<string>
using namespace std;

class Node
{
public:
	string keyword;
	string meaning;
	Node* left;
	Node* right;

	Node(string k,string m)
	{
		keyword=k;
		meaning=m;
		left=right=NULL;
	}
};

class DictionaryOp
{
public:
	Node* root=NULL;
	int count;

	void createTree();
	void addKey();
	void delKey();
	void update();
	void display(Node *root);
	void find();
};

void DictionaryOp::createTree()
{
	cout<<"\nEnter the number of words: ";
	cin>>count;

	string keyword,meaning;
	int flag=0;

	for(int i=0;i<count;i++)
	{
		cout<<"\nEnter the keyword: ";
		cin>>keyword;
		cout<<"\nEnter the meaning: ";
		cin>>meaning;
		Node* newNode=new Node(keyword,meaning);

		if(root==NULL)
		{
			root=newNode;
		}
		else
		{
			Node* parent=root;

			flag=0;

			while(flag!=1)
			{
				if(newNode->keyword)
			}
		}
	}
}

void DictionaryOp::display(Node *root)
{
	if(root==NULL)
		return;

	display(root->left);
	cout<<"\n"<<root->keyword<<": "<<root->meaning;
	display(root->right);
}

int main() {
	string one="BD",two="BD";
	cout<<"one<two"<<one.compare(two);

	return 0;
}
