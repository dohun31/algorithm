import openpyxl
import csv

def get_short_department(department):
    short_department = {
        "IT 융합응용공학과": "IT",
        "IT융합응용공학과": "IT",
        "It융합응용공학과": "IT",
        "it융합응용공학과": "IT",
        "공간정보시스템공학과": "공간정보시스템공",
        "산업경영공학과": "산업경영공",
        "시스템경영공학부": "시경",
        "전자공학과": "전자",
        "정보통신공학과": "정통",
        "컴퓨터공학과": "컴공",
        "토목공학과": "토목"
    }
    return short_department.get(department, "FixMe")


def get_short_studentid(studentid):
    return str(studentid)[2:4]


# 엑셀 불러오기
wb = openpyxl.load_workbook('2022년 1학기 개발동아리 WAP 지원서 (2).xlsx', data_only=True)
ws = wb['Sheet1']

# 읽는 엑셀 파일의 위치
nameRow = 1
departmentRow = 2
gradeRow = 4
studentIDRow = 5
phoneNumberRow = 6

# 마지막 row 셀
max_row = ws.max_row


# 기본 값들 저장
all_values = []
for index, row in enumerate(ws.rows):
    # 인덱스 열 제거
    if index == 0:
        continue
    # 이름, 학과, 학년, 학번, 연락처, 학과(short), 학번(short)
    row_value = {
        'name': row[nameRow].value,
        'department': row[departmentRow].value,
        'grade': row[gradeRow].value,
        'studentID': row[studentIDRow].value,
        'phoneNumber': row[phoneNumberRow].value,
        'department(short)': row[departmentRow].value,
        'studentID(short)': get_short_studentid(row[studentIDRow].value)
    }
    all_values.append(row_value)

# 읽기 종료
wb.close()

# 저장할 csv 파일 생성
csvFile = open('TeleListCVS_25-1.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(csvFile)
tableHeader = ['Name', 'Notes', 'Group Membership', 'Phone 1 - Value']
wr.writerow(tableHeader)

# 각 정보 재구성 및 열 추가
for member in all_values:
    # Name: 이름(WAP24-2 학과 학년 학번)
    NameValue = "WAP25-1-{}({} {} {})".format(
        member['name'],
        member['department(short)'],
        member['grade'],
        member['studentID(short)'],
    )
    # Note: WAP 24-2기 신청자 학과 학년 학번
    NoteValue = "WAP 25-1기 신청자 {} {} {}".format(
        member['department'],
        member['grade'],
        member['studentID']
    )
    # Group Membership
    GroupValue = "WAP25-1"
    # Phone 1 - Value
    PhoneNumberValue = member['phoneNumber']

    # 열 추가
    rowValues = [NameValue, NoteValue, GroupValue, PhoneNumberValue]
    wr.writerow(rowValues)

