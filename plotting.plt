reset
set term postscript enhanced color "Helvetica" 20
set yrange [0:1]
unset ytics
set ylabel "Score"
set border 31 lw 5

unset key

set boxwidth 0.5
set style fill solid

set output "Score.eps"
plot './data.dat' using 1:3:xtic(2) with boxes
set output
