#include <stdio.h>

/**
 * main - Entry point
 * Description: "basic calculator"
 * Return: Always 0 (Success)
 */
int main(){
    int n1,n2,cs;
    char op;
    printf("Enter two numbers:\n");
    scanf("%d\n%d", &n1, &n2);
    printf("Choose your operator : \"+\" \"-\" \"/\" \"*\"");
    scanf("\n%c", &op);
    switch (op) {
        case '+' : printf("%d",(n1+n2));break;
        case '-' : printf("%d",(n1-n2));break;
        case '/': printf("%d",(n1/n2));break;
        case '*' : printf("%d",(n1*n2));break;
        default : printf("Wrong operator");break;

    }
return 0;
}
