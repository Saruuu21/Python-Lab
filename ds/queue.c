#include<stdlib.h>
#include<stdio.h>
int front=-1,rear=-1;
int queue[5],data,i,size;
void insertion()
{
if(rear==size-1)
{
printf("queue is full");
}
else
{
printf("enter the data:");
scanf("%d",&data);
rear++;
queue[rear]=data;
printf("element is inserted");
if(front==-1)
{
front=0;
}
}
}
void deletion()
{
if(front==-1)
{
printf("queue is empty");
}
else
{
printf("\n popped is %d",queue[front]);
front++;
}
}
void display()
{
if(front==-1)
{
printf("queue is empty");
}
else
{
printf("elements in queue are");
for(i=front;i<=rear;i++)
{
printf("%d",queue[i]);
}
}
}
int main()
{
int ch;
printf("\n Enter the array size");
scanf("%d",&size);
do
{
printf("\n Enter your choice \n1.For insertion \n2.For deletion \n3.For display \n4.For exit\n ");
scanf("%d",&ch);
switch(ch)
{
case 1: insertion();
break;
case 2: deletion();
break;
case 3: display();
break;
case 4: exit(0);
default:
printf("invalid");
}
}
while(1);
}
