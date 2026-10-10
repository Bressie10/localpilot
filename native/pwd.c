#include <stdio.h>
#include <unistd.h>

int main() {
    char path[1024];

    char *result = getcwd(path, sizeof(path));

    if (result == NULL) {
        printf("Error PWD couldn't be found\n");
        }

    else{
        printf("%s\n", path); 
        }

    return 0;
}