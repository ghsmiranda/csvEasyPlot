python3 charts_matplot.py 'sbr_uns' 'none' 'best' -1 -1 charts_outputs/ 2 2 3 'Fatores#de#Aproxima\c{c}\~{a}o' inversion_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/r_uns.out breakpoint_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/r_uns.out
#
python3 charts_matplot.py 'sbr_sig' 'none' 'best' -1 -1 charts_outputs/ 2 2 3 'Fatores#de#Aproxima\c{c}\~{a}o' inversion_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/r_sig.out breakpoint_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/r_sig.out

python3 charts_matplot.py  'sbrt_sig' 'none' 'best' -1 -1 charts_outputs/ 2 2 3 'Fatores#de#Aproxima\c{c}\~{a}o' inversion_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/rt_sig.out breakpoint_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/rt_sig.out

python3 charts_matplot.py 'sbrt_uns' 'none' 'best' -1 -1 charts_outputs/ 2 2 3 'Fatores#de#Aproxima\c{c}\~{a}o' inversion_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/rt_uns.out breakpoint_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/rt_uns.out
#
python3 charts_matplot.py 'sbt' 'none' 'best' -1 -1 charts_outputs/ 2 2 3 'Fatores#de#Aproxima\c{c}\~{a}o' inversion_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/t.out breakpoint_algs/outputs/1000perm_n100_lamb10to100incr5/pt_version/t.out
#
xdg-open charts_outputs/sbr_uns.eps
xdg-open charts_outputs/sbr_sig.eps
xdg-open charts_outputs/sbrt_sig.eps
xdg-open charts_outputs/sbrt_uns.eps
xdg-open charts_outputs/sbt.eps

