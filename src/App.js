import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [formData, setFormData] = useState({});
  const [language, setLanguage] = useState('en-US');
  const [isRecording, setIsRecording] = useState({});
  const [submissionMessage, setSubmissionMessage] = useState(''); // new

  const questions = {
    'en-US': {
      languageSelection: "Choose a language:",
      formTitle: "Medical Form",
      personalInfo: "Personal Information",
      fullName: "Full Name",
      dateOfBirth: "Date of Birth",
      gender: "Gender",
      contactInfo: "Contact Info",
      medicalHistory: "Medical History",
      medicalConditions: "Do you have any existing medical conditions? (If yes, please specify.)",
      medications: "Are you currently taking any medications? (If yes, please list them.)",
      allergies: "Do you have any allergies? (If yes, please list them.)",
      surgeries: "Have you had any surgeries in the past? (If yes, please specify.)",
      familyHistory: "Any history of illnesses in your family? (If yes, please specify.)",
      currentHealthConcerns: "Current Health Concerns",
      symptoms: "What symptoms are you experiencing? (Please describe in detail.)",
      symptomDuration: "How long have you been experiencing these symptoms?",
      previousTreatment: "Have you received any previous treatment for this condition? (If yes, please describe.)",
      helpSeeking: "What specific help or attention are you seeking? (e.g., consultation, diagnostic tests, treatment options.)",
      lifestyleInfo: "Lifestyle Information",
      smoking: "Do you smoke or use tobacco products?",
      alcohol: "Do you consume alcohol? (If yes, how often?)",
      exercise: "Do you engage in regular exercise? (If yes, please describe your routine.)",
      diet: "What is your diet like? (Any specific dietary restrictions or preferences?)",
      appointmentDetails: "Appointment Details",
      appointmentDate: "Preferred date and time for an appointment:",
      additionalInfo: "Is there anything else you would like us to know?",
      submit: "Submit",
    },
    'fr-FR': {
      languageSelection: "Choisissez une langue :",
      formTitle: "Formulaire Médical",
      personalInfo: 'Informations personnelles',
      fullName: 'Nom complet:',
      dateOfBirth: 'Date de naissance:',
      gender: 'Genre:',
      contactInfo: 'Informations de contact (Téléphone/Email):',
      medicalHistory: 'Antécédents médicaux',
      medicalConditions: 'Avez-vous des conditions médicales existantes? (Si oui, veuillez préciser.)',
      medications: 'Prenez-vous actuellement des médicaments? (Si oui, veuillez les lister.)',
      allergies: 'Avez-vous des allergies? (Si oui, veuillez les lister.)',
      surgeries: 'Avez-vous déjà subi des interventions chirurgicales? (Si oui, veuillez préciser.)',
      familyHistory: 'Antécédents médicaux familiaux: (Maladies pertinentes dans votre famille? Si oui, veuillez préciser.)',
      currentHealthConcerns: 'Préoccupations de santé actuelles',
      symptoms: 'Quels symptômes ressentez-vous? (Veuillez décrire en détail.)',
      symptomDuration: 'Depuis combien de temps ressentez-vous ces symptômes?',
      previousTreatment: 'Avez-vous déjà reçu un traitement pour cette condition? (Si oui, veuillez décrire.)',
      helpSeeking: 'Quel type d\'aide ou d\'attention recherchez-vous? (ex: consultation, tests diagnostiques, options de traitement.)',
      lifestyleInfo: 'Informations sur le mode de vie',
      smoking: 'Fumez-vous ou utilisez-vous des produits du tabac?',
      alcohol: 'Consommez-vous de l\'alcool? (Si oui, à quelle fréquence?)',
      exercise: 'Faites-vous de l\'exercice régulièrement? (Si oui, veuillez décrire votre routine.)',
      diet: 'Quel est votre régime alimentaire? (Restrictions ou préférences alimentaires spécifiques?)',
      appointmentDetails: 'Détails du rendez-vous',
      appointmentDate: 'Date et heure préférées pour un rendez-vous:',
      additionalInfo: 'Y a-t-il autre chose que vous aimeriez que nous sachions?',
      submit: 'Soumettre',
    },
    'zh-CN': {
      languageSelection: "选择语言：",
      formTitle: "医疗表格",
      personalInfo: '个人信息',
      fullName: '全名:',
      dateOfBirth: '出生日期:',
      gender: '性别:',
      contactInfo: '联系信息（电话/电子邮件）：',
      medicalHistory: '病史',
      medicalConditions: '您有任何现有的医疗状况吗？（如果有，请具体说明。）',
      medications: '您目前正在服用任何药物吗？（如果有，请列出。）',
      allergies: '您有任何过敏吗？（如果有，请列出。）',
      surgeries: '您过去做过任何手术吗？（如果有，请具体说明。）',
      familyHistory: '家庭病史：（您家中是否有任何相关疾病？如果有，请具体说明。）',
      currentHealthConcerns: '当前健康问题',
      symptoms: '您正在经历什么症状？（请详细描述。）',
      symptomDuration: '您经历这些症状多久了？',
      previousTreatment: '您是否接受过此病症的任何先前治疗？（如果有，请描述。）',
      helpSeeking: '您希望获得什么具体帮助或关注？（例如，咨询、诊断测试、治疗方案。）',
      lifestyleInfo: '生活方式信息',
      smoking: '您吸烟或使用烟草产品吗？',
      alcohol: '您饮酒吗？（如果是，频率如何？）',
      exercise: '您定期锻炼吗？（如果是，请描述您的锻炼方式。）',
      diet: '您的饮食情况如何？（任何特定饮食限制或偏好吗？）',
      appointmentDetails: '预约详情',
      appointmentDate: '预约的首选日期和时间：',
      additionalInfo: '还有其他您想让我们知道的事情吗？',
      submit: '递交',
    },
  };

  const selectedQuestions = questions[language];

  const handleLanguageChange = (e) => {
    setLanguage(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // show confirmation message
    setSubmissionMessage("Your form has been submitted");

    // save form data to csv
    const csvData = Object.keys(formData)
      .map(key => `${key},${formData[key]}`)
      .join('\n');

    const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', 'formData.csv');
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const startSpeechRecognition = (field) => {
    if (!('webkitSpeechRecognition' in window)) {
      alert('Your browser does not support speech recognition. Please try another browser like Chrome.');
      return;
    }

    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = language;
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => {
      setIsRecording((prevState) => ({ ...prevState, [field]: true }));
      console.log('Speech recognition started');
    };

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setFormData((prevData) => ({ ...prevData, [field]: transcript }));
      setIsRecording((prevState) => ({ ...prevState, [field]: false }));
    };

    recognition.onerror = (event) => {
      console.error('Speech recognition error', event.error);
      setIsRecording((prevState) => ({ ...prevState, [field]: false }));
    };

    recognition.onend = () => {
      setIsRecording((prevState) => ({ ...prevState, [field]: false }));
      console.log('Speech recognition ended');
    };

    recognition.start();
  };

  const renderQuestions = () => {
    const fields = [
      'fullName', 'dateOfBirth', 'gender', 'contactInfo', 'medicalConditions', 'medications', 'allergies', 
      'surgeries', 'familyHistory', 'symptoms', 'symptomDuration', 
      'previousTreatment', 'helpSeeking', 'smoking', 'alcohol', 
      'exercise', 'diet', 'appointmentDate', 'additionalInfo'
    ];
    
    return (
      <>
        {fields.map((field) => (
          <div key={field}>
            <label htmlFor={field}>{selectedQuestions[field]}</label>
            <div className='field-group'>
              <input
                id={field}
                type="text"
                value={formData[field] || ''}
                onChange={(e) => setFormData({ ...formData, [field]: e.target.value })}
              />
              <button
                type="button"
                onClick={() => startSpeechRecognition(field)}
                disabled={isRecording[field]}
                className="speech-to-text-btn"
              >
                {isRecording[field] ? 'Listening...' : '🎤'}
              </button>
            </div>
          </div>
        ))}
      </>
    );
  };

  return (
    <div className="App">
      <h1>{questions[language].formTitle}</h1>
      <label htmlFor="language">{selectedQuestions.languageSelection}</label>
      <select id="language" value={language} onChange={handleLanguageChange}>
        <option value="en-US">English</option>
        <option value="fr-FR">Français</option>
        <option value="zh-CN">中文</option>
      </select>

      <form onSubmit={handleSubmit}>
        <h1>{selectedQuestions.formTitle}</h1> 
        {renderQuestions()}
        <button type="submit">{selectedQuestions.submit}</button>
      </form>

      {submissionMessage && <p className="submission-message">{submissionMessage}</p>}
    </div>
    
    
  
  );
}

export default App;
