import time
import random

def get_weather_info(destination, travel_date):
    if "3" in travel_date or "4" in travel_date or "5" in travel_date:
        season, desc = "봄", "날씨가 온화해서 여행하기 정말 좋아요. 가벼운 외투를 챙기세요!"
    elif "6" in travel_date or "7" in travel_date or "8" in travel_date:
        season, desc = "여름", "기온이 높고 활기찬 계절이에요. 자외선 차단제는 필수입니다!"
        if "상하이" in destination or "도쿄" in destination:
            desc = "매우 덥고 습할 수 있으니 통풍이 잘 되는 옷과 휴대용 선풍기를 챙기세요!"
    elif "9" in travel_date or "10" in travel_date or "11" in travel_date:
        season, desc = "가을", "선선한 바람이 불어 산책하기 좋고 야경이 예쁜 시기예요."
    else:
        season, desc = "겨울", "날씨가 쌀쌀하니 따뜻한 옷차림으로 감기 조심하세요!"
    
    return f"[{season}] {desc}"

def start_travel_program(departure, destination, travel_month):
    print(f"\n🌐 {travel_month}, [{departure}] 🛫 [{destination}] 실시간 정보를 분석 중입니다...")
    time.sleep(1)

    # 1. 항공권 상세 데이터 생성 (날짜/시간 추가)
    airlines = ["제주항공", "진에어", "티웨이", "대한항공", "아시아나", "에어부산"]
    flight_results = []
    
    # 입력받은 달의 날짜를 랜덤하게 생성 (예: 15일, 22일 등)
    for airline in airlines:
        day = random.randint(1, 28) # 랜덤 날짜
        hour = random.randint(6, 22) # 랜덤 시간 (06시~22시)
        minute = random.choice([0, 15, 30, 45]) # 15분 단위
        price = random.randint(80, 250) * 1000 # 8만 원 ~ 25만 원 사이
        
        flight_results.append({
            "airline": airline,
            "date": f"{travel_month} {day}일",
            "time": f"{hour:02d}:{minute:02d}",
            "price": price
        })

    # 가격순 정렬
    sorted_flights = sorted(flight_results, key=lambda x: x['price'])

    # 2. 날씨 가이드 호출
    weather_desc = get_weather_info(destination, travel_month)

    # 3. 결과 출력
    print("\n" + "="*70)
    print(f"✈️  {departure} -> {destination} 최저가 항공권 스케줄")
    print("="*70)
    print(f"{'순위':<4} | {'출발 날짜':<8} | {'출발 시간':<6} | {'가격':<10} | {'항공사'}")
    print("-" * 70)
    
    for i, f in enumerate(sorted_flights[:5], 1):
        time.sleep(0.2)
        print(f"{i:2d}위 | {f['date']:<10} | {f['time']:<8} | {f['price']:8,}원 | {f['airline']}")
    
    print("-" * 70)
    print(f"🌤️  {destination} 현지 기후 가이드")
    print(f"👉 {weather_desc}")
    print("="*70)

if __name__ == "__main__":
    print("\n[ ✈️ 스마트 여행 플래너 v6.0 ]")
    start = input("1. 출발지: ")
    end = input("2. 목적지: ")
    month = input("3. 여행 달 (예: 8월): ")
    
    if start.strip() and end.strip() and month.strip():
        start_travel_program(start, end, month)
    else:
        print("정보를 모두 입력해 주세요!")