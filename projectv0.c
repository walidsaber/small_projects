#include <stdio.h>

/**
 * main - Entry point
 * Description: "Prints a Floyd's Triangle"
 * Return: Always 0 (Success)
 */
int main(){
    int i, j,p,q;
    int inp;
    printf("enter num of rows:\n");
    scanf("%d", &inp);
    for (i = 1; i<=inp;i++){
        if(i%2==0){
            p=1;
            q=0;
        }else{
            p=0;
            q=1;
        }
        for (j=1;j<=i;j++){
            if((j%2)!=0){
                printf("%d",p);
            }else{
                printf("%d",q);

            }
        }
        printf("\n");
    }
return 0;
}
