#include<stdio.h>
int main()
{
int a,b,c;
printf("\n Enter the a,b,c");
scanf("%d%d%d",&a,&b,&c);
if(a<=b)
   if(b<=c)
printf("c is large");
    else
printf("b is large");

else
printf("a is large");
printf("\n");
return 0;
}

