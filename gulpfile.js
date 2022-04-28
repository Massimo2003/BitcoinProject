import {spawn} from 'node:child_process';
import gulp from 'gulp';

const {watch, series} = gulp;

let myProcess = null;

const watcher = async () => {
    watch(['./**/*.js'], series(stop, start));
};

const start = async () => {
    myProcess = spawn('node', ['test.py'], {stdio: 'inherit'});
};

const stop = async () => {
    if (myProcess) {
        await myProcess.kill();
        myProcess = null;
    }
};
