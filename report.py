def generate_report(total_users, sequence_counts, anomalies):
    print(f"총 {total_users}명의 사용자가 활동했습니다.\n")

    if sequence_counts:
        top_seq = max(sequence_counts, key=sequence_counts.get)
        top_count = sequence_counts[top_seq]
        print("가장 많이 나타난 행동 흐름:")
        print(f"- {top_seq} ({top_count}명)\n")

    if any(anomalies.values()):
        print("이상 행동이 감지되었습니다.\n")

        for rule, users in anomalies.items():
            if users:
                print(f"- {rule}: {len(users)}명 ({', '.join(users)})")
    else:
        print("이상 행동은 감지되지 않았습니다.")