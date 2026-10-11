//Imports
#include <stdio.h>
#include <libproc.h>
#include <stdbool.h>
#include <unistd.h>
#include <string.h>

//PS function
int psFunc(const char *desired_processes) {
    if (desired_processes != NULL && strcmp(desired_processes, "-u") != 0) {
        printf("Please enter a valid arguemnt");
        return 1;
    } 

    
    int userId = getuid();
    int i;
    int processIds[1024];

    int sizeOfProcessIds =  proc_listpids(
            PROC_ALL_PIDS,
            0,
            processIds, 
            sizeof(processIds)
            );

    
    int numOfPIDS = sizeOfProcessIds / sizeof(processIds[0]);
    
    for (i = 0; i < numOfPIDS; i++) {


        char processName[256];
        int success_code = proc_name(
            processIds[i],
            processName,
            sizeof(processName)
        );
        if (success_code == 0) {
            continue;
            }

        struct proc_bsdinfo info;
        int result_proc_code = proc_pidinfo(
            processIds[i],
            PROC_PIDTBSDINFO,
            0,
            &info,
            sizeof(info)
        );

        if (result_proc_code == 0) {
            continue;
        }

        if (desired_processes != NULL) {
            if (strcmp(desired_processes, "-u") == 0 && userId != info.pbi_uid) {
                continue;
            }}

        printf("PID : %d | Name: %s\n", processIds[i], processName);
        }

        return 0;
    }


int main(int argc, char *argv[]) {
    int ps_success_code;
    if (argc == 1) {
        ps_success_code = psFunc(NULL);
    }
    else if (argc == 2){
        ps_success_code = psFunc(argv[1]);
    }
    else {
        printf("Too many arguments given");
        return 1;
    }
    return ps_success_code;
}


