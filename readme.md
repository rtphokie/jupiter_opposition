Calculates opposition dates for Jupiter via Skyfield, using the JPL developmental ephemeris 421, identifying
the most recent opposition that was closer and the next one that will be closer.

Created to support story on the 2024 opposition of Jupiter for WRAL-TV in Raleigh, NC.

https://www.wral.com/story/jupiter-shines-big-and-bright-at-opposition/21757987/

```
/Users/trice/PycharmProjects/jupiter_opposition/.venv/bin/python -X pycache_prefix=/Users/trice/Library/Caches/JetBrains/PyCharm2024.1/cpython-cache /Applications/PyCharm.app/Contents/plugins/python/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --client 127.0.0.1 --port 50325 --file /Users/trice/PycharmProjects/jupiter_opposition/jupiterdistance.py 
Connected to pydev debugger (build 241.19416.19)
Jupiter oppositions
                                                                                           closest
  distance (mi)                           date     ang dia                          since                          until
    384,790,666       Tue Jul 14 03:58:26 2020       46.57       Sun Dec  2 20:45:07 2012       Thu Aug 19 20:28:30 2021
    373,050,895       Thu Aug 19 20:28:30 2021       48.04       Fri Oct 28 21:41:54 2011       Mon Sep 26 15:33:08 2022
    367,421,095       Mon Sep 26 15:33:08 2022       48.77       Tue Oct  8 06:59:11 1963                               
    370,209,765       Fri Nov  3 01:02:26 2023       48.41       Mon Sep 26 15:33:08 2022       Sun Oct  1 20:58:24 2034
    380,161,047       Sat Dec  7 15:58:00 2024       47.14       Fri Nov  3 01:02:26 2023       Thu Aug 25 01:40:00 2033
    393,375,102       Sat Jan 10 03:42:09 2026       45.56       Sat Dec  7 15:58:00 2024       Mon Jul 19 04:33:40 2032
    405,393,429       Wed Feb 10 19:28:48 2027       44.21       Sat Jan 10 03:42:09 2026       Sun Jun 15 05:19:41 2031
    412,755,756       Sun Mar 12 11:36:49 2028       43.42       Wed Feb 10 19:28:48 2027       Mon May 13 07:33:11 2030
    413,568,883       Thu Apr 12 00:04:56 2029       43.33       Sun Mar 12 11:36:49 2028       Mon May 13 07:33:11 2030
    407,646,849       Mon May 13 07:33:11 2030       43.96       Wed Feb 10 19:28:48 2027       Sun Jun 15 05:19:41 2031
    396,433,900       Sun Jun 15 05:19:41 2031       45.20       Sat Jan 10 03:42:09 2026       Mon Jul 19 04:33:40 2032
    383,099,806       Mon Jul 19 04:33:40 2032       46.78       Sat Dec  7 15:58:00 2024       Thu Aug 25 01:40:00 2033
    372,031,853       Thu Aug 25 01:40:00 2033       48.17       Fri Nov  3 01:02:26 2023       Sun Oct  1 20:58:24 2034
    367,468,035       Sun Oct  1 20:58:24 2034       48.77       Mon Sep 26 15:33:08 2022                               
    371,276,112       Thu Nov  8 00:42:34 2035       48.27       Sun Oct  1 20:58:24 2034       Sat Oct  6 20:29:14 2046
    381,813,445       Fri Dec 12 09:42:22 2036       46.94       Thu Nov  8 00:42:34 2035       Wed Aug 30 02:02:30 2045
    395,016,412       Thu Jan 14 14:57:41 2038       45.37       Fri Dec 12 09:42:22 2036       Sun Jul 24 01:54:54 2044
    406,522,436       Tue Feb 15 03:02:12 2039       44.08       Thu Jan 14 14:57:41 2038       Fri Jun 19 21:36:14 2043
    413,098,486       Fri Mar 16 16:58:28 2040       43.38       Tue Feb 15 03:02:12 2039       Sat May 17 18:54:38 2042
    413,138,268       Tue Apr 16 07:20:57 2041       43.38       Fri Mar 16 16:58:28 2040       Sat May 17 18:54:38 2042
    406,605,752       Sat May 17 18:54:38 2042       44.07       Tue Feb 15 03:02:12 2039       Fri Jun 19 21:36:14 2043
    395,106,587       Fri Jun 19 21:36:14 2043       45.36       Thu Jan 14 14:57:41 2038       Sun Jul 24 01:54:54 2044
    381,871,101       Sun Jul 24 01:54:54 2044       46.93       Fri Dec 12 09:42:22 2036       Wed Aug 30 02:02:30 2045
    371,339,969       Wed Aug 30 02:02:30 2045       48.26       Thu Nov  8 00:42:34 2035       Sat Oct  6 20:29:14 2046
    367,570,706       Sat Oct  6 20:29:14 2046       48.75       Sun Oct  1 20:58:24 2034                               
    372,149,797       Tue Nov 12 21:11:31 2047       48.15       Sat Oct  6 20:29:14 2046                               
    383,139,221       Thu Dec 17 00:32:40 2048       46.77       Tue Nov 12 21:11:31 2047                               
```