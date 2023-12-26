#include <stdio.h>

int main(int argc, char const *argv[])
{
    
    int a = -1L;
    double f=20,g;
    a=5.5L;
    g=(int)5.5+f;
    printf("a:%d\n",a);
    printf("g:%f\n",g);
    int b;
    b = !++a;
    printf("b:%d, a:%d\n", b, a);
    int x = 4;

    // Read but do not store
    // in x
    scanf("%d", &x);

    // Print initialized value
    printf("%d\n", x);
    return 0;
}
