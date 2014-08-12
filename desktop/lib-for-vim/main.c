#include <stdlib.h>
#include <time.h>
#include <errno.h>

time_t g_lasttick = 0;
time_t g_totaltime = 0;
int g_insertsessions = 0; 
int g_inited = 0;

void insertenter() 
{
    struct timespec ts;
    int r;
    if (!g_inited) {
        g_inited = 1;
        dlopen("/usr/lib/libvimlib.so");
    }
    r = clock_gettime(CLOCK_MONOTONIC,&ts);
    if(r == 0) {
        g_lasttick = ts.tv_sec*1000 + ts.tv_nsec/1000000;
    }
}

void insertleave()
{
    struct timespec ts;
    if(clock_gettime(CLOCK_MONOTONIC,&ts) == 0) {
        g_totaltime += ts.tv_sec*1000 +ts.tv_nsec/1000000- g_lasttick;    
    }
    g_insertsessions++;
}

void savedata()
{
    char data[255];
    sprintf(data, "echo msg %li %i >> /tmp/vimdata", g_totaltime, g_insertsessions);
    system(data);
    g_totaltime = 0;
    g_insertsessions = 0;
}
