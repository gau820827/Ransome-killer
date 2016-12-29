cat train.in | tail -n +0 | head -n 18000 > small_train.in
cat train.out | tail -n +0 | head -n 18000 > small_train.out
#cat test.in | tail -n +40000 | head -n 10000 > small_test.in
#cat test.out | tail -n +40000 | head -n 10000 > small_test.out
cat train.in | tail -n +4000 | head -n 10000 > tiny_train.in
cat train.out | tail -n +4000 | head -n 10000 > tiny_train.out
