gregorian_to_jalali(){
    gy=$1; gm=$2; gd=$3
    g_d_m=(0 31 59 90 120 151 181 212 243 273 304 334)
    if [ $gm -gt 2 ]; then
        gy2=$((gy + 1))
    else
        gy2=$gy
    fi
    days=$((355666 + (365 * gy) + ((gy2 + 3) / 4) - ((gy2 + 99) / 100) + ((gy2 + 399) / 400) + gd + g_d_m[gm - 1]))
    jy=$((-1595 + (33 * (days / 12053))))
    days=$((days % 12053))
    jy=$((jy + (4 * (days / 1461))))
    days=$((days % 1461))
    if [ $days -gt 365 ]; then
        jy=$((jy + ((days - 1) / 365)))
        days=$(((days - 1) % 365))
    fi
    if [ $days -lt 186 ]; then
        jm=$((1 + (days / 31)))
        jd=$((1 + (days % 31)))
    else
        jm=$((7 + ((days - 186) / 30)))
        jd=$((1 + ((days - 186) % 30)))
    fi

    jalali=($jy $jm $jd)
}

##############ZIP################

gregorian_to_jalali $(date '+%Y %m %d');
filedatetime=${jalali[0]}${jalali[1]}${jalali[2]}_$(date +%H%M%S);
echo $datetime
