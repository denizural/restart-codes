#!/usr/bin/env bash

# ===
# global variables
# ===
PREFIX=$(whoami)
NFILES=25
CHECK_MODE=false
VERBOSE_MODE=false
fname=""

# ===
# process command line arguments
# ===
while getopts "cvp:n:" arg; do
    case ${arg} in
        c) # check mode (eg. dry run)
            CHECK_MODE=true
            echo "check mode is on"
            ;;
        v) # verbose mode
            VERBOSE_MODE=true
            echo "verbose is on"
            ;;
        p) # prefix
            PREFIX=${OPTARG}
            ;;
        n) # number of files
            NFILES=${OPTARG}
            ;;
        ?) # invalid option
            echo "ERROR: invalid option"
            exit 1
    esac
done


get_last_file_number() {
    prefix=$1

    # if no files are found, then return 0
    files=$(ls -1v ${prefix}* 2>/dev/null)
    if [[ $? != 0 ]]; then
        if [[ ${VERBOSE_MODE} == true ]]; then
            echo "0 files are found so far for $1"
        fi
        return 0
    fi

    last_number=$(ls -1v ${prefix}* | tail -n 1 | sed "s/${prefix}//")
    nfiles=$(ls ${prefix}* | wc -l)
    if [[ ${VERBOSE_MODE} == true ]]; then
        echo "${nfiles} files are found so far for $1"
    fi

    return ${last_number}
}


main() {
    start_number=0

    # check the last file number
    get_last_file_number ${PREFIX}
    ret_val=$?
    if [[ ${ret_val} != 0 ]]; then
        start_number=$(expr ${ret_val} + 1)
    fi

    end_number=$(expr ${start_number} + ${NFILES} - 1)
    if [[ VERBOSE_MODE == true ]]; then
        echo "start number: ${start_number}"
        echo "end number: ${end_number}"
    fi
    for index in $(seq ${start_number} ${end_number}); do
        fname="${PREFIX}${index}"
        if [[ ${VERBOSE_MODE} == true || ${CHECK_MODE} == true ]]; then
            echo "Creating the file ${fname}"
        fi
        if [[ ${CHECK_MODE} == false ]]; then
            touch ${fname}
        fi
    done
}

# ===
# main program
# ===
main
