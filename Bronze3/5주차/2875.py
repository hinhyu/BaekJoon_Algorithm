#대회 or 인턴
#2명의 여학생과 1명의 남학생이 팀,
#대회에 참여하려는 학생들 중 K명은 반드시 인턴쉽 프로그램에 참여해야 한다. 인턴쉽에 참여하는 학생은 대회에 참여하지 못한다.
#만들 수 있는 팀의 최대 개수을 출력하면 된다.

n, m, k = map(int, input().split())
cnt = 0
while n >= 0 and m >= 0 and n + m >= k:
    n -= 2
    m -= 1
    cnt += 1
print(cnt-1) #cnt로 출력하면 n,m이 0이 되었을 때도 추가됨