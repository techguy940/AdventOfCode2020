data = """1593
1575
1583
1609
1835
2008
1638
1396
1833
1524
1778
1574
1653
1962
1831
1557
1847
1587
1876
1914
1565
1585
1713
35
1862
1885
1735
1497
1989
1871
1923
1917
1719
1797
1222
1493
1939
1139
1260
1622
1625
1683
1742
1996
1579
1703
1692
1920
1536
1965
1936
1947
1800
1556
1633
1530
1612
1764
1810
1845
1750
1854
1973
1512
1856
1568
1634
1630
1602
1555
1681
1844
1544
1909
1690
1851
1785
863
1866
1988
1715
1881
1570
1380
1956
777
1693
1717
1724
1975
790
1484
1822
1922
1963
1741
1809
1896
1837
1980
1244
1832
1834
1643
1775
1818
1503
1802
1957
1174
1826
1649
1941
1571
1930
1629
1502
2002
1700
1880
1723
1803
2007
1543
1872
1993
1740
1919
1688
1067
1680
1580
1558
1772
1694
1480
1257
1796
2001
537
1701
1613
1784
1559
1482
1968
1604
983
1842
1817
1850
1788
1982
1535
1615
453
1895
1443
1308
1533
1714
1765
1037
1992
1843
1883
1981
1525
1038
1540
1766
1886
1546
1716
810
1899
1708
1508
1870
1051
1867
1840
1617
1726
1566
1616
1948
1771
1627
1994
1486
1913
1600
1983
1501
2003
1667
1620
1943
1674""".splitlines()

data = list(map(int, data))

for i in data:
  for j in data:
      for a in data:
        if i+j+a == 2020:
          print(i, j, a, i*j*a)
          break
