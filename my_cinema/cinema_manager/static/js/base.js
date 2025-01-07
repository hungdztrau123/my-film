// let hideTimeoutLoading;

// const boxLoading = document.getElementById('box-loading');
// clearTimeout(hideTimeoutLoading);
// hideTimeoutLoading = setTimeout(() => {
//     boxLoading.style.display = 'none'; 
// }, 500);


//Ẩn loading khi trang đã tải xong
window.addEventListener('load', function() {
    var loadingBox = document.getElementById('box-loading');
    setTimeout(function() {
        loadingBox.style.display = 'none'; 
    }, 500);
});


function getPromoFilm() {
    fetch('/api/films/?status__iexact=Now&ordering=-updated_at')
        .then(response => response.json())
        .then(data => {
        const filmList = document.getElementById('promotion-image-film-base-list');


        // Tạo các phần tử phim
        data.results.slice(0,1).forEach(film => {
            const filmItem = document.createElement('div');
            filmItem.classList.add('promotion-image-film-base-item');
            filmItem.innerHTML = `
                
                <img src="${film.promo}" alt="${film.name}" class="promotion-image-film-base">
                
            `;
            filmItem.addEventListener('click', () => {
                window.location.href = `/film/${film.id}/`;
            });
            filmList.appendChild(filmItem);
        });
        })
        .catch(error => {
        console.error('Error fetching film data:', error);
        });

}

getPromoFilm();



const btnCancelFilm = document.querySelector('.box-cancel-promotion-image-film-base');
const boxPromoFilm = document.querySelector('.box-promotion-image-film-base');
btnCancelFilm.addEventListener('click', () => {
    boxPromoFilm.style.display = 'none';
});


let hideTimeout;
let hideTimeoutFilm;

document.addEventListener('scroll', function () {
    const navbar = document.getElementById('header-base');
    const backButton = document.querySelector('.icon-back-base');
    const promoFilm = document.querySelector('.promotion-image-film-base-list');
    const btnCancelFilm = document.querySelector('.box-cancel-promotion-image-film-base');

    // Hiện thẻ back button khi cuộn qua navbar
    if (window.scrollY >= navbar.offsetHeight) {
        backButton.style.display = 'block'; // Hiện thẻ back button
        promoFilm.style.display = 'block';
        btnCancelFilm.style.display = 'block';

        // Reset timeout để ẩn thẻ back button
        clearTimeout(hideTimeout);
        hideTimeout = setTimeout(() => {
            backButton.style.display = 'none'; // Ẩn thẻ back button sau 3 giây
        }, 3000);

        clearTimeout(hideTimeoutFilm);
        hideTimeoutFilm = setTimeout(() => {
            promoFilm.style.display = 'none'; 
            btnCancelFilm.style.display = 'none';
        }, 6000);


    } else {
        backButton.style.display = 'none'; // Ẩn thẻ back button nếu không cuộn qua navbar
        promoFilm.style.display = 'none';
        btnCancelFilm.style.display = 'none';
        clearTimeout(hideTimeout); // Xóa timeout nếu cuộn lên
        clearTimeout(hideTimeoutFilm);
    }
});

// Hiển thị back button khi hover vào

const backButton = document.querySelector('.icon-back-base');
backButton.addEventListener('mouseover', function () {
    clearTimeout(hideTimeout); // Xóa timeout ẩn
    backButton.style.display = 'block'; // Hiện thẻ back button
});

backButton.addEventListener('mouseout', function () {
    // Kiểm tra điều kiện để ẩn lại thẻ back button
    if (window.scrollY >= document.getElementById('header-base').offsetHeight) {
        hideTimeout = setTimeout(() => {
            backButton.style.display = 'none'; // Ẩn thẻ back button sau 3 giây
        }, 3000);
    }
});



const promoFilm = document.querySelector('.promotion-image-film-base-list');
promoFilm.addEventListener('mouseover', function () {
    clearTimeout(hideTimeoutFilm); // Xóa timeout ẩn
    promoFilm.style.display = 'block'; // Hiện thẻ 
    btnCancelFilm.style.display = 'block';
});



promoFilm.addEventListener('mouseout', function () {
    // Kiểm tra điều kiện để ẩn lại thẻ back button
    if (window.scrollY >= document.getElementById('header-base').offsetHeight) {
        hideTimeoutFilm = setTimeout(() => {
            promoFilm.style.display = 'none'; // Ẩn thẻ back button sau 3 giây
            btnCancelFilm.style.display = 'none';
        }, 6000);
    }
});


btnCancelFilm.addEventListener('mouseover', function () {
    clearTimeout(hideTimeoutFilm); // Xóa timeout ẩn
    promoFilm.style.display = 'block'; // Hiện thẻ 
    btnCancelFilm.style.display = 'block';
});


btnCancelFilm.addEventListener('mouseout', function () {
    // Kiểm tra điều kiện để ẩn lại thẻ back button
    if (window.scrollY >= document.getElementById('header-base').offsetHeight) {
        hideTimeoutFilm = setTimeout(() => {
            promoFilm.style.display = 'none'; // Ẩn thẻ back button sau 3 giây
            btnCancelFilm.style.display = 'none';
        }, 6000);
    }
});



// Ẩn thẻ back button ban đầu
document.addEventListener('DOMContentLoaded', function () {
    backButton.style.display = 'none';
    promoFilm.style.display = 'none';
    btnCancelFilm.style.display = 'none';
});



document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById('box-icon-chat-box');
    const boxTopFilm = document.getElementById('chatbox');

    button.addEventListener('click', function () {
        if (boxTopFilm.style.display === 'none' || boxTopFilm.style.display === '') {
            boxTopFilm.style.display = 'block';
        } else {
            boxTopFilm.style.display = 'none';
        }
    });

    // Thiết lập trạng thái ban đầu cho box-top-film
    boxTopFilm.style.display = 'none';
});





async function sendMessage() {
    const accessToken = localStorage.getItem('access_token');

    const userInput = document.getElementById('userInput');
    const message = userInput.value;
    if (!message) return;
    appendMessage(message, 'user');

    // Giả lập phản hồi từ API
    setTimeout(async () => {
        const response = await getBotResponse(message);
        appendMessage(response, 'bot');
    }, 1000);

    userInput.value = '';
}

let messageCount = 0;

function appendMessage(message, sender) {
    const messagesDiv = document.getElementById('messages');
    const messageDiv = document.createElement('div');
    messageCount++;
    messageDiv.className = 'message ' + sender + ' chatfilm' + messageCount;
    console.log("bababa", messageDiv.className);
    messageDiv.innerText = message;



    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

async function getBotResponse(input) {
    const apiKey = 'afe06fe2';
    const accessToken = localStorage.getItem('access_token');


    const greetings = ['chào'];
    const filmNows = ['phim'];
    const scheduleDays = ['lịch', 'ngày'];
    const promotions = ['quảng cáo', 'khuyến mãi'];



    if (greetings.some(greeting => input.toLowerCase().includes(greeting))) {
        return "CINEPLEX ODEON xin chào! Bạn muốn tìm kiếm phim đang chiếu rạp nào ?";
    }

    // Kiểm tra từ khóa lịch trình hoặc ngày chiếu
    else if (scheduleDays.some(scheduleDay => input.toLowerCase().includes(scheduleDay))) {
        fetch('/api/schedules/?status__iexact=Có hiệu lực')
            .then(response => response.json())
            .then(data => {
                messageCount;
                const scheduleListClass = `.message.bot.chatfilm${messageCount}`;
                console.log("kjdslfjsdfj", scheduleListClass);
                const scheduleList = document.querySelector(scheduleListClass);
                scheduleList.innerHTML = `<span class="chat-response-top">Các lịch trình chiếu phim:</span> `;

                // Tạo các phần tử phim
                data.results.forEach((schedule, index) => {


                    const date = new Date(schedule.dayshow ? schedule.dayshow.day : '');
                    const day = String(date.getDate()).padStart(2, '0'); // Lấy ngày và thêm số 0 nếu cần
                    const month = String(date.getMonth() + 1).padStart(2, '0'); // Lấy tháng (tháng bắt đầu từ 0)
                    const year = date.getFullYear(); // Lấy năm
                    const formattedDate = `${day}/${month}/${year}`; // Định dạng ngày


                    function formatTime(timeString) {
                        const timeCustom = new Date(timeString);
                        return timeCustom.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
                    }


                    const scheduleItem = document.createElement('div');
                    scheduleItem.classList.add('chat-schedule-item');


                    scheduleItem.innerHTML = `
                            
                                    <span class="schedule-chat-time"><span class="label-schedule-chat-time">Lịch trình: </span> ${formatTime(schedule.start_time)} ~ ${formatTime(schedule.end_time)}</span>
                                    </br>
                                    <span class="schedule-chat-film"><span class="label-schedule-chat-film">Phim: </span> ${schedule.film ? schedule.film.name : ''}</span>
                                    </br>
                                    <span class="schedule-chat-day"><span class="label-schedule-chat-day">Ngày chiếu:</span> ${formattedDate}</span>
                                    </br>
                                    <span class="schedule-chat-area"><span class="label-schedule-chat-area">Khu vực:</span> ${schedule.place ? schedule.place.area.name : ''}</span>
                                    </br>
                                    <span class="schedule-chat-place"><span class="label-schedule-chat-place">Rạp:</span> ${schedule.place ? schedule.place.name : ''}</span>
                                    </br>
                                    <span class="schedule-chat-room"><span class="label-schedule-chat-room">Phòng:</span> ${schedule.room ? schedule.room.name : ''}</span>
                                    



                               
                        `;

                    scheduleItem.addEventListener('click', () => {
                        window.location.href = `/film/${schedule.film.id}/`;
                    });

                    scheduleList.appendChild(scheduleItem);
                });
            })
            .catch(error => {
                console.error('Error fetching schedule data:', error);
            });

    }



    // Gọi API để phân tích câu hỏi
    //const movieResponse = await fetch(`http://www.omdbapi.com/?i=tt3896198&s=${input}&apikey=${apiKey}`);
    //const movieData = await movieResponse.json();

    //if (movieData.Response === "True") {
    //    return `Tìm thấy phim: ${movieData.Search.map(movie => movie.Title).join(', ')}`;
    //}

    //return 'Không tìm thấy phim nào.';




    else if (filmNows.some(filmNow => input.toLowerCase().includes(filmNow))) {
        fetch('/api/films/?status__iexact=Now')
            .then(response => response.json())
            .then(data => {
                messageCount;
                const filmListClass = `.message.bot.chatfilm${messageCount}`;
                console.log("kjdslfjsdfj", filmListClass);
                const filmList = document.querySelector(filmListClass);
                filmList.innerHTML = `<span class="chat-response-top">Các phim đang chiếu:</span>
                    `;

                // Tạo các phần tử phim
                data.results.forEach((film, index) => {
                    const filmItem = document.createElement('div');
                    filmItem.classList.add('chat-film-item');


                    filmItem.innerHTML = `
                            
                                    <span class="film-chat-name"><i class="fa-solid fa-film"></i> ${film.name}\n</span>
                               
                        `;

                    filmItem.addEventListener('click', () => {
                        window.location.href = `/film/${film.id}/`;
                    });

                    filmList.appendChild(filmItem);
                });
            })
            .catch(error => {
                console.error('Error fetching film data:', error);
            });
    }

    else if (promotions.some(promotion => input.toLowerCase().includes(promotion))) {
        fetch('/api/promotions/?ordering=-updated_at')
            .then(response => response.json())
            .then(data => {
                messageCount;
                const promotionListClass = `.message.bot.chatfilm${messageCount}`;
                console.log("kjdslfjsdfj", promotionListClass);
                const promotionList = document.querySelector(promotionListClass);
                promotionList.innerHTML = `<span class="chat-response-top">Các quảng cáo của tôi:</span>
                    `;

                // Tạo các phần tử phim
                data.results.forEach((promotion, index) => {

                    function formatDate(dateString) {
                        const date = new Date(dateString);
                        const day = String(date.getDate()).padStart(2, '0');
                        const month = String(date.getMonth() + 1).padStart(2, '0');
                        const year = date.getFullYear();
                        return `${day}/${month}/${year}`;
                    }

                    const promotionItem = document.createElement('div');
                    promotionItem.classList.add('chat-promotion-item');


                    promotionItem.innerHTML = `
                            
                                    <span class="promotion-chat-name"><span class="label-promotion-chat-name">Tiêu đề:</span> ${promotion.name}</span>
                                    
                                    <span class="promotion-chat-start"><span class="label-promotion-chat-start">Ngày bắt đầu:</span> ${formatDate(promotion.start_date)}</span>
                                    
                                    <span class="promotion-chat-end"><span class="label-promotion-chat-end">Ngày kết thúc:</span> ${formatDate(promotion.end_date)}</span>
                                    
                                    

                               
                        `;

                    promotionItem.addEventListener('click', () => {
                        window.location.href = `/promotion/${promotion.id}/`;
                    });

                    promotionList.appendChild(promotionItem);
                });
            })
            .catch(error => {
                console.error('Error fetching promotion data:', error);
            });
    }



    else {
        fetch(`/api/films/?name__icontains=${encodeURIComponent(input)}&status__in=Now,Coming`)
            .then(response => response.json())
            .then(data => {
                messageCount;
                const movieListClass = `.message.bot.chatfilm${messageCount}`;
                console.log("kjdslfjsdfj", movieListClass);
                const movieList = document.querySelector(movieListClass);


                movieList.innerHTML = ''; // Xóa nội dung cũ

                if (data.results.length > 0) {
                    movieList.innerHTML = `<span class="chat-response-top">Tìm thấy phim:</span>
                    `;

                    // Tạo các phần tử phim
                    data.results.forEach((movie) => {
                        const movieItem = document.createElement('div');
                        movieItem.classList.add('chat-movie-item');

                        movieItem.innerHTML = `
                            <span class="movie-chat-name"><i class="fa-solid fa-film"></i> ${movie.name}</span>
                            </br>
                        `;

                        movieItem.addEventListener('click', () => {
                            window.location.href = `/film/${movie.id}/`;
                        });

                        movieList.appendChild(movieItem);
                    });
                } else {
                    movieList.innerHTML = 'Không tìm thấy phim nào.';
                }




            })
            .catch(error => {
                console.error('Error fetching movie data:', error);
            });

    }




}


document.getElementById('userInput').addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

document.getElementById('btn-sent-chat').addEventListener('click', () => {

    sendMessage();

});







const toggleButton = document.getElementById('toggle-button');
const baseDiv = document.getElementById('base');
const headerBaseDiv = document.getElementById('header-base');



let isDarkMode = localStorage.getItem('isDarkMode') === 'true' || false;

// Hàm để cập nhật giao diện
function updateTheme() {
    if (isDarkMode) {
        toggleButton.textContent = 'Light';
        toggleButton.style.color = '#d5a12c';
        toggleButton.style.textShadow = '1px 1px 1px #000';
        toggleButton.style.backgroundColor = '#fff';

        baseDiv.style.color = '#d5a12c';
        baseDiv.style.textShadow = '1px 1px 1px #000';
        headerBaseDiv.style.textShadow = '1px 1px 1px #000';


    } else {
        toggleButton.textContent = 'Dark';
        toggleButton.style.color = '#d5a12c';
        toggleButton.style.textShadow = '1px 1px 1px #fff';
        toggleButton.style.backgroundColor = '#000';

        baseDiv.style.color = '#d5a12c';
        baseDiv.style.textShadow = '1px 1px 1px #000';

    }

    // Cập nhật hình nền dựa trên chế độ
    fetch('/api/backgrounds/')
        .then(response => response.json())
        .then(data => {
            if (data.results.length > 0) {
                const imageUrl = data.results[0].image; // Lấy image từ phần tử đầu tiên
                baseDiv.style.background = `url(${imageUrl}) ${isDarkMode ? '#000' : '#fff'}`;
                
               

            }
        })
        .catch(error => {
            console.error('Error fetching background data:', error);
        });


}

window.addEventListener('DOMContentLoaded', () => {
    updateTheme();
});

toggleButton.addEventListener('click', () => {
    isDarkMode = !isDarkMode;
    localStorage.setItem('isDarkMode', isDarkMode);
    updateTheme();
});




const sessionName = localStorage.getItem('session_name');
const sessionId = localStorage.getItem('session_id');

// Kiểm tra access token khi tải trang
const accessToken = localStorage.getItem('access_token');

if (accessToken) {
    document.getElementById('session-info').innerText = `Xin chao : ${sessionName}`;
    document.getElementById('session-id-user').innerText = `${sessionId}`;

    // Nếu có access token, hiển thị nút Logout và ẩn nút Login
    document.getElementById('logout-btn').style.display = 'flex';
} else {
    document.getElementById('box-session-info').style.display = 'none';
    // Nếu không có access token, hiển thị nút Login
    document.getElementById('login-btn').style.display = 'flex';
}

const boxSessionInfo = document.getElementById('box-session-info');
const boxContentUser = document.getElementById('box-content-user');


boxSessionInfo.addEventListener('click', function (event) {
    if (boxContentUser.style.display === 'flex') {
        boxContentUser.style.display = 'none';
    } else {
        boxContentUser.style.display = 'flex';
    }
    event.stopPropagation();
});

document.addEventListener('click', function () {
    boxContentUser.style.display = 'none';
});

document.getElementById('content-user-item-info').addEventListener('click', function () {
    window.location.href = `/infouser/${sessionId}/`;
    localStorage.removeItem('activeTabBase');
});

document.getElementById('content-user-item-ticket').addEventListener('click', function () {
    window.location.href = `/listticket/${sessionId}/`;
    localStorage.removeItem('activeTabBase');
});

document.getElementById('navbar-homepage').addEventListener('click', function () {
    window.location.href = '/homepage/';
});
document.getElementById('navbar-area').addEventListener('click', function () {
    window.location.href = '/area/';
});
document.getElementById('navbar-promotionlist').addEventListener('click', function () {
    window.location.href = '/promotionlist/';
});
document.getElementById('navbar-contact').addEventListener('click', function () {
    window.location.href = '/contact/';
});

document.getElementById('login-btn').addEventListener('click', function () {
    localStorage.removeItem('activeTabBase');
    window.location.href = '/login/';
});

document.getElementById('logout-btn').addEventListener('click', function () {

    const accessToken = localStorage.getItem('access_token');
    const refreshToken = localStorage.getItem('refresh_token');


    if (refreshToken) {
        fetch('/api/logout/', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${accessToken}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ refresh: refreshToken }),
        })
            .then(response => {
                if (response.ok) {
                    localStorage.removeItem('access_token');  // Xóa access token
                    localStorage.removeItem('refresh_token'); // Xóa refresh token
                    localStorage.removeItem('session_name');
                    localStorage.removeItem('is_admin');
                    localStorage.removeItem('activeTab');
                    localStorage.removeItem('activeTabBase');


                    window.location.href = '/login/'; // Chuyển hướng về trang đăng nhập

                } else if (response.status === 401) {
                    alert('Token đã hết hạn. Vui lòng đăng nhập lại.');
                    localStorage.removeItem('access_token');
                    localStorage.removeItem('refresh_token');
                    localStorage.removeItem('session_name');
                    localStorage.removeItem('is_admin');
                    localStorage.removeItem('activeTab');
                    localStorage.removeItem('activeTabBase');


                    window.location.href = '/login/'; // Chuyển hướng về trang đăng nhập

                } else {
                    alert('Logout failed! Please try again.');
                    localStorage.removeItem('access_token');
                    localStorage.removeItem('refresh_token');
                    localStorage.removeItem('session_name');
                    localStorage.removeItem('is_admin');
                    localStorage.removeItem('activeTab');
                    localStorage.removeItem('activeTabBase');


                    window.location.href = '/login/'; // Chuyển hướng về trang đăng nhập
                }
            })
            .catch(error => {
                console.error('Error during logout:', error);
                alert('Logout failed! Please try again later.');
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                localStorage.removeItem('session_name');
                localStorage.removeItem('is_admin');
                localStorage.removeItem('activeTab');
                localStorage.removeItem('activeTabBase');


                window.location.href = '/login/'; // Chuyển hướng về trang đăng nhập
            });
    } else {
        alert('You are not logged in.');
        window.location.href = '/login/';
    }
});


// Lấy danh sách promotions từ API
fetch('/api/promotions/?ordering=-updated_at')
    .then(response => response.json())
    .then(data => {
        const promotionList = document.getElementById('promotion-banner');

        // Tạo các phần tử promotion
        data.results.slice(0, 2).forEach(promotion => {
            const promotionItem = document.createElement('div');
            promotionItem.classList.add('promotion-item');
            promotionItem.innerHTML = `
                <div class="box-promotion-img">
                    <img src="${promotion.banner}" class="promotion-img" alt="${promotion.name}">
                </div>
            `;
            promotionItem.addEventListener('click', () => {
                window.location.href = `/promotion/${promotion.id}/`;
            });
            promotionList.appendChild(promotionItem);
        });
    })
    .catch(error => {
        console.error('Error fetching promotion data:', error);
    });



fetch('/api/logos/')
    .then(response => response.json())
    .then(data => {
        const logoList = document.getElementById('logo-cinema');

        // Tạo các phần tử logo
        data.results.slice(0, 1).forEach(logo => {
            const logoItem = document.createElement('div');
            logoItem.classList.add('logo-item');
            logoItem.innerHTML = `
                    <img src="${logo.image}" class="logo-img" alt="${logo.name}">
            `;
            logoItem.addEventListener('click', () => {
                window.location.href = `/home/`;
                localStorage.removeItem('activeTabBase');
            });
            logoList.appendChild(logoItem);
        });


        const logoFooterList = document.getElementById('footer-logo-cinema');

        // Tạo các phần tử logo
        data.results.slice(0, 1).forEach(logoFooter => {
            const logoFooterItem = document.createElement('div');
            logoFooterItem.classList.add('footer-logo-item');
            logoFooterItem.innerHTML = `
                    <img src="${logoFooter.image}" class="footer-logo-img" alt="${logoFooter.name}">
            `;
            logoFooterItem.addEventListener('click', () => {
                window.location.href = `/home/`;
                localStorage.removeItem('activeTabBase');
            });
            logoFooterList.appendChild(logoFooterItem);
        });

    })
    .catch(error => {
        console.error('Error fetching logo data:', error);
    });






// Đặt màu sắc cho item được chọn
function setActiveTab(activeId) {
    const itemsNavBase = document.querySelectorAll('.content-navbar');


    // Xóa màu sắc khỏi tất cả các item bên trái và bên phải
    itemsNavBase.forEach(item => item.classList.remove('text-color-base'));


    // Thêm màu sắc cho item được chọn
    const activeItemNavBase = document.getElementById(activeId);
    activeItemNavBase.classList.add('text-color-base');


}

// Lưu trạng thái tab đã chọn vào localStorage
function saveActiveTab(activeId) {
    localStorage.setItem('activeTabBase', activeId);
}

// Lấy trạng thái tab đã chọn từ localStorage
function loadActiveTab() {
    const activeId = localStorage.getItem('activeTabBase');
    if (activeId) {
        setActiveTab(activeId);
    }
}

// Gán sự kiện click cho từng item bên trái
document.querySelectorAll('.content-navbar').forEach(item => {
    item.addEventListener('click', function () {
        const id = this.id;
        saveActiveTab(id); // Lưu tab hoạt động
        window.location.href = `/${id.replace('navbar-', '')}/`; // Chuyển trang
    });
});



// Tải trạng thái tab khi trang được tải
window.onload = loadActiveTab;

