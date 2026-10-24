# 메디픽 사이트 배포 안내

도메인 없이 무료 주소(`메디픽이름.netlify.app`)로 먼저 사이트를 열고, 문의 폼이 joon@agon.kr로 오게 하는 순서입니다. 도메인은 나중에 사서 연결하면 됩니다. 4단계까지 전부 무료입니다.

| 단계 | 할 일 | 걸리는 시간 |
|---|---|---|
| 1 | 문의 폼 연결 키 받기 (Web3Forms) | 2분 |
| 2 | 사이트 올리기 (Netlify, 무료 주소) | 5분 |
| 3 | 문의 폼 테스트 | 2분 |
| 4 | (나중에) 도메인 사서 연결하기 | 20분 + 반영 대기 |
| 5 | 공개 직전: 검색 노출 켜기 (Google·네이버) | 20분 |

---

## 1. 문의 폼 연결 키 받기

문의 폼 내용은 Web3Forms라는 무료 서비스를 거쳐 이메일로 전달됩니다. 서버가 따로 필요 없습니다.

1. https://web3forms.com 에 접속합니다.
2. **Create your Access Key** 칸에 `joon@agon.kr`을 입력하고 키를 요청합니다.
3. joon@agon.kr 메일함에 온 **Access Key**(영문·숫자로 된 긴 값)를 복사합니다. 메일이 안 보이면 스팸함도 확인하세요.
4. `index.html`에서 아래 줄을 찾아 따옴표 안에 키를 붙여넣습니다.

   ```js
   var FORM_KEY = '';
   ```

   예: `var FORM_KEY = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx';`

> 키를 Claude에게 알려주면 대신 넣어줄 수 있습니다. 이 키는 웹페이지에 공개되어도 되는 값입니다. 메일을 받을 주소만 정해져 있고, 계정 비밀번호가 아닙니다.

## 2. 사이트 올리기 (Netlify, 무료 주소)

올릴 사이트는 `index.html`, `robots.txt`, `sitemap.xml` 파일과 `img` 폴더입니다. 새 폴더를 하나 만들어 이것들만 넣어 두세요.

1. https://app.netlify.com 에서 가입합니다. 이메일이나 GitHub 계정으로 가입할 수 있습니다.
2. https://app.netlify.com/drop 에 접속해 그 폴더를 통째로 끌어다 놓습니다.
3. 몇 초 뒤 `무작위이름.netlify.app` 주소가 생깁니다. 열어서 사이트가 잘 나오는지 확인합니다.
4. **Site configuration → Change site name**에서 이름을 `medipick`처럼 바꿉니다. 사이트 주소가 `https://medipick.netlify.app`이 됩니다. 이미 누가 쓰는 이름이면 `medipick-kr`처럼 바꿔보세요.
5. 사이트 주소가 들어간 곳(5단계 표 참고)에서 `https://kimjoonnnn.github.io/medipick` 부분을 정해진 주소로 바꾸고 폴더를 다시 올립니다. 이렇게 하면 카카오톡 등에 링크를 보낼 때 병원 사진 미리보기가 뜹니다.

   예: `<meta property="og:image" content="https://medipick.netlify.app/img/derm-lobby.jpg">`

수정한 내용을 다시 올릴 때는 Netlify 사이트 화면의 **Deploys** 탭에 폴더를 다시 끌어다 놓으면 됩니다. HTTPS(자물쇠)는 자동으로 켜집니다.

## 3. 문의 폼 테스트

1. 올린 사이트 맨 아래 **문의 남기기** 폼에 테스트 내용을 적어 보냅니다.
2. "문의가 접수됐어요" 문구가 나오는지 확인합니다.
3. joon@agon.kr에 `[메디픽 문의]`로 시작하는 메일이 왔는지 확인합니다. 처음 한두 통은 스팸함으로 갈 수 있으니, 스팸이 아님으로 표시해 두세요.
4. 받은 메일에서 **답장**을 누르면 문의한 사람의 이메일로 바로 회신됩니다.

---

## 4. (나중에) 도메인 연결하기

### 도메인 고르기

- **새로 사기**: 가비아(gabia.com), 후이즈(whois.co.kr) 같은 곳에서 `medipick.kr`, `medipick.co.kr` 같은 주소를 검색해 삽니다. 보통 1년 단위로 결제합니다.
- **agon.kr 하위 주소 쓰기**: joon@agon.kr 메일을 쓰고 있다면 agon.kr 도메인은 이미 회사 누군가가 관리하고 있을 가능성이 큽니다. 관리하는 사람에게 `medipick.agon.kr` 같은 하위 주소를 하나 만들어 달라고 하면 돈을 들이지 않고 쓸 수 있습니다.

### 연결하기

1. Netlify 사이트 화면에서 **Domain management → Add a domain**을 누르고 도메인을 입력합니다.
2. Netlify가 보여주는 DNS 값을 도메인을 산 곳의 **DNS 관리** 화면에 입력합니다. **반드시 Netlify 화면에 나온 값을 그대로 쓰세요.**

   | 경우 | 종류 | 호스트(이름) | 값 |
   |---|---|---|---|
   | 새 도메인 (예: medipick.kr) | A | `@` | Netlify가 알려주는 IP 주소 |
   | 새 도메인의 www | CNAME | `www` | `사이트이름.netlify.app` |
   | 하위 주소 (예: medipick.agon.kr) | CNAME | `medipick` | `사이트이름.netlify.app` |

3. 반영까지 몇 분에서 몇 시간 걸립니다. 연결되면 HTTPS가 자동으로 켜집니다.
4. 사이트 주소가 들어간 곳(5단계 표 참고)을 새 주소로 바꾸고 다시 올립니다.

### ⚠️ agon.kr을 건드릴 때 꼭 지킬 것

- **MX 레코드는 절대 지우거나 바꾸지 마세요.** MX는 이메일 수신 설정이라, 건드리면 joon@agon.kr 메일이 안 들어올 수 있습니다.
- TXT 레코드(SPF 등)도 그대로 두세요.
- 하위 주소용 CNAME 하나만 추가하면 기존 설정에 영향이 없습니다.

---

## 5. 공개 직전: 검색 노출 켜기

지금은 사이트가 열려 있어도 Google·네이버 검색에는 나오지 않게 막아 두었습니다. 공개할 때 아래 순서로 켭니다.

### 사이트 주소가 들어간 곳

도메인을 바꿀 때는 아래를 모두 새 주소로 바꿉니다. 하나라도 빠지면 검색엔진이 예전 주소를 대표 주소로 볼 수 있습니다.

| 파일 | 위치 |
|---|---|
| `index.html` | `<link rel="canonical">`, `og:url`, `og:image`, 아래쪽 `<script type="application/ld+json">` 안의 `url`·`image`·`logo` |
| `robots.txt` | `Sitemap:` 줄 |
| `sitemap.xml` | `<loc>` 줄 |

### 켜는 순서

1. `index.html` 맨 위의 `<meta name="robots" content="noindex, nofollow">` 줄과 그 위 설명 주석을 지웁니다. **이 줄이 남아 있으면 검색에 절대 나오지 않습니다.**
2. `sitemap.xml`의 `<lastmod>` 날짜를 공개일로 바꿉니다.
3. **Google Search Console** (https://search.google.com/search-console)에 사이트를 등록합니다. 소유 확인용 `<meta name="google-site-verification" ...>` 태그를 받으면 `index.html`의 `<head>` 안에 넣고 다시 올린 뒤 확인을 누릅니다. 그다음 **Sitemaps** 메뉴에 `sitemap.xml` 주소를 제출합니다.
4. **네이버 서치어드바이저** (https://searchadvisor.naver.com)에도 똑같이 등록합니다. `<meta name="naver-site-verification" ...>` 태그를 넣고, **요청 → 사이트맵 제출**에 `sitemap.xml` 주소를 넣습니다.
5. 카카오톡 링크 미리보기는 처음 보낸 내용이 저장됩니다. 사진이나 문구를 바꾼 뒤에는 카카오 공유 디버거(https://developers.kakao.com/tool/debugger/sharing)에서 주소를 넣고 **캐시 초기화**를 누릅니다.

> 공개 전에 `robots.txt`에 `Disallow`를 넣지 마세요. 검색엔진이 페이지를 아예 못 읽으면 `noindex` 표시도 못 보고, 다른 곳의 링크만으로 주소가 검색에 뜰 수 있습니다.
>
> `robots.txt`는 도메인 맨 앞(`medipick.kr/robots.txt`)에 있어야 검색엔진이 읽습니다. 지금 주소(`kimjoonnnn.github.io/medipick/`)에서는 읽히지 않으니, 도메인을 연결하기 전까지는 3·4번에서 사이트맵을 직접 제출하면 됩니다.

---

## 참고

- **개인정보 동의 문구**: 폼에는 "보유 기간: 문의 처리 후 1년"으로 들어가 있습니다. 회사 방침에 맞게 `index.html`에서 바꾸세요.
- **스팸 방지**: 사람 눈에 안 보이는 함정 칸이 들어가 있어 단순한 스팸 봇은 걸러집니다. 스팸이 많아지면 Web3Forms 설정에서 추가 차단을 켤 수 있습니다.
- **claude.ai 미리보기 링크**에서는 보안 정책 때문에 폼 전송이 되지 않습니다. 폼은 Netlify에 올린 사이트에서만 작동합니다.
