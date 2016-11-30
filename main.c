
#include <stdio.h>
#include <omp.h>
#include <stdlib.h>
#include <string.h>

double fib (int n)
{
    if (n == 1 || n == 2 || n == 0)
    {
        return 1;
    }
    else
    {
        return fib(n-1) + fib(n-2);
    }
}

double  fib_two (int n)
{
    double  a =0, b = 1;
    int i;
    for(i = 1; i<n; i++)
    {
        double t = b+a;
        a = b;
        b = t;

    }
    return  b;
}
int main(int argc, char ** argv)
{
    if (argc != 3)
    {
        fprintf(stderr, "Need two arguments");

        return (1);
    }

    int numberfib = atoi(argv[2]);

    if (strcmp(argv[1], "recursive") == 0)
    {
        double timeone = omp_get_wtime();
//        fprintf(f,"%f\n", fib(numberfib));
        fib(numberfib);
        double timetwo = omp_get_wtime();
        fprintf(stdout,"%.20f\n", timetwo - timeone);
    }
    else if (strcmp(argv[1], "iterative") == 0)
    {
        double timeone = omp_get_wtime();
//        fprintf(f,"%f\n", fib_two(numberfib));
        fib_two(numberfib);
        double timetwo = omp_get_wtime();
        fprintf(stdout,"%.20f\n", timetwo - timeone);
    }
    else
    {
        fprintf(stderr, "Invalid argument");
        return (1);
    }


    return 0;
}

