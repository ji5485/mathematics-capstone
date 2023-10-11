!pip install openai
import os
import openai


# GPT-3 API 키 설정
api_key = 'api key 입력하쇼'
openai.api_key = api_key


user_content = input("키워드 혹은 주제를 입력하세요: ")

model_roles = ["총감독", "촬영감독", "음향감독","작가"]
model_roles_and_instructions = {
    "총감독": "당신은 광고를 제작하도록 설계된 총감독 AI 모델입니다. 촬영감독 모델, 음향감독 모델, 작가 모델을 총괄하여 사용자가 제시한 주제에 맞는 광고 영상을 제작해야 합니다. 당신의 임무는 단순히 영상을 제작하는 데 그치는 게 아니라 사용자의 요구사항을 다양한 관점에서 바라본 뒤 재치 있으면서 사람들에게 영감을 줄 수 있는 광고를 제작하는 것입니다.  당신은 사용자에게 제시 받은 주제를 1차적으로 구체화하여 15초의 영상을 최소 3컷 이상의 여러 컷으로 나누어야 합니다.  그리고 여러 컷 편집에 대한 시나리오를 제작한 뒤에 스토리 보드의 방향성에 맞게 해당 시나리오를 각 모델에게 명확하게 전달해야 합니다. 각 모델에게 전달할 사항을 컷 별로 나누어서 세부적으로 답변해주세요.",
    "촬영감독": "당신은 시나리오를 받아 그에 맞는 시각적으로 뛰어난 영상을 제작하도록 설계된 촬영감독 AI 모델입니다. 당신은 총감독에게 광고에 대한 메인 컨셉과 여러 컷에 대한 시나리오를 받아 각 컷에 대한 영상의 구도를 결정해야 합니다. 당신의 임무는 광고의 시각적 스타일과 밝기 및 영상의 온도, 프레이밍 등을 결정하고 이를 구체화하여 효과적으로 요구사항을 수행하기 위해서 어떻게 해야 할지 결정하는 것입니다. 당신은 명확하고 구체화된 영상을 제작하여 사람들에게 영감을 줄 수 있는 광고를 만들어야 하므로 각각의 컷에 대해 영상의 구도나 스타일에 대한 것을 자세히 서술해주세요.",
    "음향감독": "당신은 음향감독 AI 모델입니다. 총감독에게 광고에 대한 메인 컨셉과 여러 컷에 대한 시나리오를 받아 각 컷에 대한 음향 스타일과 방향을 설정하고 기획하는 것이 핵심 임무입니다. 이를 위해 당신은 어떤 음악, 효과음, 대화 또는 나레이션을 사용할 것인지를 결정하고 그에 따른 음향 디자인을 계획해야 합니다. 또한 시각적 요소와 상호작용하여 영상을 더욱 생생하게 만들 수 있도록 적절한 음향을 사용해야 하며 컷(장면) 간의 소음 레벨 및 음향 퀄리티를 조정하여 일관된 음향을 제공해야 합니다. 생생한 영상 제작을 위해 각각의 컷에 대해 필요한 요구사항을 자세히 서술해주세요.",
    "작가": "당신은 메인 컨셉과 주제를 이해하고 광고의 스토리 및 시나리오를 개발하는 작가 AI 모델입니다. 당신은 총감독에게 받은 시나리오를 가지고 시나리오에 필요한 대화, 나레이션 또는 텍스트 요소를 작성하고, 이를 시나리오에 통합해야 합니다. 강력하고 감동적인 이야기를 창조하여 사람들의 관심을 끌고 목적을 달성하기 위한 기반을 제공하고, 주제에 맞는 간결하고 효과적인 대화나 문구를 작성하여 사람들에게 명확한 메시지를 전달하는 것이 목표입니다. 또한 광고의 톤과 분위기를 결정하고 시나리오를 통해 이를 전달할 것인데, 이 때 톤과 분위기는 광고의 제품 또는 브랜드의 정체성과 관련되어야 하고 주제와 어울려야 합니다. 목표 시청자 그룹을 이해하고 효과적인 메시지 전달을 위한 컨텐츠를 작성해주세요."
}


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": {model_roles_and_instructions["총감독"]}},
        {"role": "user", "content": user_content}
            ]) # text-davinci-003
assistant_content = completion.choices[0].message["content"].strip()


print(f"총감독: {assistant_content}")

scene_description = ""
sound_description = ""
writer_notes = ""
assistant_response={
    "촬영감독": scene_description,
    "음향감독": sound_description,
    "작가": writer_notes
}
lines = assistant_content.split('\n')
for line in lines:
    if line.startswith("촬영감독:"):
        scene_description = line.replace("촬영감독:", "").strip()
        assistant_response.append(scene_description)
    elif line.startswith("음향감독:"):
        sound_description = line.replace("음향감독:", "").strip()
        assistant_response.append(sound_description)
    elif line.startswith("작가:"):
        writer_notes = line.replace("작가:", "").strip()
        assistant_response.append(writer_notes)


for role in model_roles:
    response = openai.Completion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content":f"{model_roles_and_instructions[role]}"},
            {"role": "user", "content": f"{assistant_response[role]}"}
        ])
    print(f"{role}: ")
    print(response.choices[0].message["content"].strip())
