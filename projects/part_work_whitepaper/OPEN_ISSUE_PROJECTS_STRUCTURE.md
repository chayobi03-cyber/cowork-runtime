# Open Issue — projects/ 서브 항목 운영 기준 (P4-02, 미해결 기록)

> 이 문서는 해결책이 아니라 **이슈 기록**이다. 창엽님이 "나중에 정리하자"고 명시적으로 미룬
> 사항을 다음 세션에서 잊지 않도록 남겨둔다.

## 이슈

cowork-runtime 저장소의 `projects/` 하위에는 현재 `mvp_school/`, `traceable_emc_agent_system/`,
`part_work_whitepaper/`가 동일 레벨로 존재한다. 그런데 이 셋의 성격이 다르다.

- `mvp_school/`: School이라는 **운영 체계 자체**(GPT 측 병렬 운영 포함)
- `traceable_emc_agent_system/`: School을 거쳐 Main Track으로 승급한 **실행 코드 프로젝트**
- `part_work_whitepaper/`: School에 **재학 중인 Work Package 하나**(WP-0001)

즉 `mvp_school/`은 "학교 건물"이고 `part_work_whitepaper/`는 "그 학교에 다니는 학생 한 명"에
가까운데, 지금은 폴더 구조상 둘이 형제로 나란히 있다. Work Package가 더 늘어나면
(WP-0002, WP-0003...) 이 구조가 유지 가능한지 불명확하다.

## 후보 방향 (판단 아님, 참고용 나열만)

1. 현행 유지 — projects/ 밑에 전부 나란히 두고, roster(Google Sheets)가 실제 목록 역할
2. `projects/school_work_packages/part_work_whitepaper/` 처럼 Work Package를 하위 폴더로 모음
3. `mvp_school/`에 Work Package 목록/링크만 두고 실제 내용은 각 Work Package 폴더가 소유

## 다음 세션 확인사항

- Work Package(WP-xxxx)가 2개 이상으로 늘어나는 시점에 이 이슈를 다시 꺼낸다
- 그 전까지는 현행(옵션 1)으로 유지, 별도 결정 불필요
